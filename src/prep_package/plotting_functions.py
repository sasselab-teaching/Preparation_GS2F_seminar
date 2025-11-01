import numpy as np
import matplotlib.pyplot as plt
import sklearn.linear_model as linear_model



def plot_2d_scatter_with_fits(x, phenotype=None, figsize=(7, 3.5), save_path=None, models=True):
    """
    Plot one or more scatter plots with optional linear regression fits.

    Pairing logic and panels:
    - If x is a single array and phenotype is a single array -> one panel.
    - If x is a list of arrays and phenotype is a single array -> one panel per x against the same phenotype.
    - If x is a single array and phenotype is a list of arrays -> one panel per phenotype against the same x.
    - If x and phenotype are lists of equal length -> pair elementwise; number of panels equals the number of pairs.

    Parameters:
    -----------
    x : array-like or list of array-like
        Independent variable(s). If a list, multiple subplots will be created.
    phenotype : array-like or list of array-like, optional
        Dependent variable(s). Required. If a single array, it will be reused for all x arrays.
    figsize : tuple or None, optional
        Figure size (width, height). If None, computed based on number of subplots.
    save_path : str, optional
        Path to save the figure. If None, figure is not saved.
    models : None | True | sklearn model | list/tuple of models, optional
        - None: Only plot scatter plots without fits
        - True: Fit LinearRegression models within the function (default)
        - sklearn model: Single pre-fitted model for the single-plot case
        - list/tuple: Pre-fitted models per subplot (length must equal number of panels)

    Returns:
    --------
    fig : matplotlib.figure.Figure
    ax : numpy.ndarray of matplotlib.axes.Axes (length equals number of subplots)
    models_out : list of fitted/used models or None
        List aligns with subplots order. None if models is None.
    """
    def _is_list_like(a):
        return isinstance(a, (list, tuple))

    if phenotype is None:
        raise ValueError("phenotype must be provided for plotting.")

    # Normalize x to list form if needed
    if _is_list_like(x):
        xs = [np.asarray(xi) for xi in x]
    else:
        xs = [np.asarray(x)]

    # Normalize phenotype to list form if needed
    if _is_list_like(phenotype):
        ys = [np.asarray(y) for y in phenotype]
    else:
        ys = [np.asarray(phenotype)]

    # Build plotting pairs according to rules
    pairs = []
    if len(xs) == 1 and len(ys) == 1:
        pairs = [(xs[0], ys[0])]
    elif len(xs) > 1 and len(ys) == 1:
        pairs = [(xi, ys[0]) for xi in xs]
    elif len(xs) == 1 and len(ys) > 1:
        pairs = [(xs[0], yi) for yi in ys]
    else:
        if len(xs) != len(ys):
            raise ValueError("When providing lists for both x and phenotype, their lengths must match.")
        pairs = list(zip(xs, ys))

    xlabels = [f'X{i+1}' for i in range(len(pairs))]
    y_label = 'Phenotype'
    default_colors = ['blue', 'green', 'purple', 'orange', 'teal']

    n_plots = len(pairs)

    # Compute default figsize if not provided
    if figsize is None:
        figsize = (3.5 * n_plots, 3.5)

    fig, ax = plt.subplots(1, n_plots, figsize=figsize)
    axes = np.atleast_1d(ax)

    # Normalize models parameter for iteration
    use_models = models is not None
    models_out = [] if use_models else None

    for i, (xi, yi) in enumerate(pairs):
        color = default_colors[i % len(default_colors)]
        axes[i].scatter(xi, yi, color=color, alpha=0.6)
        axes[i].set_xlabel(xlabels[i])
        axes[i].set_ylabel(y_label)
        axes[i].spines['top'].set_visible(False)
        axes[i].spines['right'].set_visible(False)

        if use_models:
            # Determine model to use for this subplot
            if models is True:
                mdl = linear_model.LinearRegression()
                mdl.fit(xi.reshape(-1, 1), yi)
            elif _is_list_like(models):
                if len(models) <= i:
                    raise ValueError("Provided models list/tuple length is less than number of subplots.")
                mdl = models[i]
            else:
                # Single model provided - valid only for single-plot case
                if n_plots != 1:
                    raise ValueError("Single model provided but multiple subplots detected. Provide a list/tuple of models matching the number of subplots.")
                mdl = models

            # Plot regression line and R^2 annotation
            x_fit = np.linspace(xi.min(), xi.max(), 100)
            y_fit = mdl.predict(x_fit.reshape(-1, 1))
            axes[i].plot(x_fit, y_fit, color='red', linewidth=2)
            try:
                r2 = mdl.score(xi.reshape(-1, 1), yi)
                coef = getattr(mdl, 'coef_', [np.nan])[0]
                intercept = getattr(mdl, 'intercept_', np.nan)
                axes[i].text(0.05, 0.95, f'$R^2$ = {r2:.2f}\n$y$ = {coef:.2f}x + {intercept:.2f}', 
                             transform=axes[i].transAxes, verticalalignment='top')
            except Exception:
                # If model doesn't implement score/coef_/intercept_
                pass

            models_out.append(mdl)

    if save_path:
        fig.savefig(save_path, dpi=300, bbox_inches='tight')

    return fig, axes, (models_out if use_models else None)

# New: Flexible 3D scatter with optional plane fit
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401

def plot_3d_scatter_with_plane(x1, x2, y, figsize=(7, 5), model=True, grid_res=10, elev=20, azim=-45, 
                                surface_alpha=0.5, point_color='purple', surface_color='orange', save_path=None):
    """
    Plot a 3D scatter of (x1, x2, y) with an optional fitted plane.

    Parameters:
    -----------
    x1, x2 : array-like
        Independent variables.
    y : array-like
        Dependent variable.
    figsize : tuple, optional
        Figure size (width, height).
    model : None | True | fitted model, optional
        - None: only scatter, no plane
        - True: fit sklearn LinearRegression inside the function (default)
        - fitted model: either sklearn LinearRegression or statsmodels OLSResults
    grid_res : int, optional
        Resolution of the plane meshgrid.
    elev, azim : float, optional
        View angles.
    surface_alpha : float, optional
        Transparency of the plane surface.
    point_color, surface_color : str, optional
        Colors for points and plane.
    save_path : str, optional
        Path to save the figure.

    Returns:
    --------
    fig, ax, model_out
        model_out is the used/fitted model or None if model is None.
    """
    x1 = np.asarray(x1)
    x2 = np.asarray(x2)
    y = np.asarray(y)

    # Decide on model usage
    model_out = None
    if model is True:
        mdl = linear_model.LinearRegression()
        X = np.column_stack((x1, x2))
        mdl.fit(X, y)
        model_out = mdl
    elif model is None:
        mdl = None
        model_out = None
    else:
        mdl = model
        model_out = model

    fig = plt.figure(figsize=figsize)
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x1, x2, y, color=point_color, alpha=0.6)
    ax.set_xlabel('Independent Variable 1 (x1)')
    ax.set_ylabel('Independent Variable 2 (x2)')
    ax.set_zlabel('Phenotype')

    # Prepare grid and predictions if a model is available
    if mdl is not None:
        x1_grid, x2_grid = np.meshgrid(np.linspace(x1.min(), x1.max(), grid_res),
                                       np.linspace(x2.min(), x2.max(), grid_res))
        X_grid = np.column_stack((x1_grid.ravel(), x2_grid.ravel()))

        # Predict based on model type (sklearn or statsmodels)
        try:
            # sklearn style
            y_grid = mdl.predict(X_grid).reshape(x1_grid.shape)
            r2 = mdl.score(np.column_stack((x1, x2)), y)
            coef1 = getattr(mdl, 'coef_', [np.nan, np.nan])[0]
            coef2 = getattr(mdl, 'coef_', [np.nan, np.nan])[1]
            intercept = getattr(mdl, 'intercept_', np.nan)
        except Exception:
            # statsmodels style
            import statsmodels.api as sm
            y_grid = mdl.predict(sm.add_constant(X_grid)).reshape(x1_grid.shape)
            r2 = getattr(mdl, 'rsquared', np.nan)
            params = getattr(mdl, 'params', [np.nan, np.nan, np.nan])
            intercept, coef1, coef2 = params[0], params[1], params[2]

        ax.plot_surface(x1_grid, x2_grid, y_grid, color=surface_color, alpha=surface_alpha)
        ax.text2D(0.05, 0.95, f'$R^2$ = {r2:.2f}\n$y$ = {coef1:.2f}x1 + {coef2:.2f}x2 + {intercept:.2f}', transform=ax.transAxes)

    ax.view_init(elev=elev, azim=azim)

    if save_path:
        fig.savefig(save_path, dpi=300, bbox_inches='tight')

    return fig, ax, model_out

# New: Flexible boxplot with statistical tests for group comparisons
from scipy.stats import ranksums, ttest_ind, mannwhitneyu

def plot_grouped_boxplots(variables, groups, figsize=(7.5, 4), test='ranksums', 
                          group_labels=None, var_labels=None, colors=None,
                          ylabel='Value', save_path=None):
    """
    Plot boxplots comparing groups across one or multiple variables with statistical tests.

    Parameters:
    -----------
    variables : array-like or list of array-like
        Single variable or list of variables to plot. Each variable should have same length as groups.
    groups : array-like (boolean or categorical)
        Group assignments. If boolean, True = positive group, False = negative group.
        If categorical, will use unique values as groups.
    figsize : tuple, optional
        Figure size (width, height). If None, computed based on number of variables.
    test : str or None, optional
        Statistical test to use: 'ranksums' (Wilcoxon rank-sum, default), 'ttest' (t-test), 
        'mannwhitneyu' (Mann-Whitney U), or None (no test).
    group_labels : list of str, optional
        Labels for groups. If None, uses ['Positive', 'Negative'] for boolean or unique group values.
    var_labels : list of str, optional
        Labels for variables. If None, uses ['Variable 1', 'Variable 2', ...].
    colors : list of str or None, optional
        Colors for each group. If None, uses ['blue', 'red'].
    ylabel : str, optional
        Y-axis label.
    save_path : str, optional
        Path to save the figure.

    Returns:
    --------
    fig, axes, test_results
        fig: matplotlib figure
        axes: array of axes
        test_results: list of (statistic, pvalue) tuples for each variable
    """
    def _is_list_like(a):
        return isinstance(a, (list, tuple))

    # Normalize inputs
    if not _is_list_like(variables):
        variables = [variables]
    variables = [np.asarray(v) for v in variables]
    groups = np.asarray(groups)
    
    n_vars = len(variables)
    
    # Validate all variables have same length as groups
    for i, var in enumerate(variables):
        if len(var) != len(groups):
            raise ValueError(f"Variable {i} length ({len(var)}) doesn't match groups length ({len(groups)})")
    
    # Determine group structure
    unique_groups = np.unique(groups)
    if len(unique_groups) != 2:
        raise ValueError("Currently only supports binary group comparisons (2 unique groups)")
    
    # Set up group labels
    if group_labels is None:
        if groups.dtype == bool:
            group_labels = ['Positive', 'Negative']
            group1_mask = groups
            group2_mask = ~groups
        else:
            group_labels = [str(g) for g in unique_groups]
            group1_mask = groups == unique_groups[0]
            group2_mask = groups == unique_groups[1]
    else:
        if groups.dtype == bool:
            group1_mask = groups
            group2_mask = ~groups
        else:
            group1_mask = groups == unique_groups[0]
            group2_mask = groups == unique_groups[1]
    
    # Set up variable labels
    if var_labels is None:
        var_labels = [f'Variable {i+1}' if n_vars > 1 else 'Variable' for i in range(n_vars)]
    
    # Set up colors
    if colors is None:
        colors = ['blue', 'red']
    
    # Compute figsize if not provided
    if figsize is None:
        figsize = (3.75 * n_vars, 4)
    
    # Create subplots
    fig, ax = plt.subplots(1, n_vars, figsize=figsize)
    axes = np.atleast_1d(ax)
    
    # Statistical test function
    test_func = None
    if test == 'ranksums':
        test_func = ranksums
    elif test == 'ttest':
        test_func = ttest_ind
    elif test == 'mannwhitneyu':
        test_func = mannwhitneyu
    elif test is not None:
        raise ValueError(f"Unknown test: {test}. Use 'ranksums', 'ttest', 'mannwhitneyu', or None")
    
    test_results = []
    
    for i, (var, var_label) in enumerate(zip(variables, var_labels)):
        # Split data by groups
        group1_data = var[group1_mask]
        group2_data = var[group2_mask]
        
        # Create boxplots
        bp1 = axes[i].boxplot(group1_data, positions=[1], widths=0.6, 
                              boxprops=dict(color=colors[0]), 
                              medianprops=dict(color=colors[0]))
        bp2 = axes[i].boxplot(group2_data, positions=[2], widths=0.6, 
                              boxprops=dict(color=colors[1]), 
                              medianprops=dict(color=colors[1]))
        
        axes[i].set_xticklabels(group_labels)
        axes[i].set_title(var_label)
        axes[i].set_ylabel(ylabel)
        axes[i].spines['top'].set_visible(False)
        axes[i].spines['right'].set_visible(False)
        
        # Perform statistical test if requested
        if test_func is not None:
            stat, pvalue = test_func(group1_data, group2_data)
            test_results.append((stat, pvalue))
            
            # Add p-value annotation
            max_val = max(var.max(), group1_data.max(), group2_data.max())
            axes[i].text(1.5, max_val * 0.9, f'p = {pvalue:.3e}', ha='center')
        else:
            test_results.append((None, None))
    
    if save_path:
        fig.savefig(save_path, dpi=300, bbox_inches='tight')
    
    return fig, axes, test_results