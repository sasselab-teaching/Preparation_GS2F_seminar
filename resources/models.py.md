We’ll create a `model_training.py` script that:

1. Uses **argparse** to accept training parameters (e.g., epochs, batch size, learning rate).
2. Loads a model class from `models.py`.
3. Loads data from provided train/val paths.
4. Trains the model using **PyTorch Lightning**.

Here’s a structured example for `model_training.py`:

```python
# model_training.py
import argparse
import torch
from torch.utils.data import DataLoader, random_split, Dataset
import pytorch_lightning as pl
from pytorch_lightning.loggers import TensorBoardLogger
from models import get_model  # assumes models.py defines get_model(name, **kwargs)


# Example dataset (you would replace with real data loading logic)
class SimpleDataset(Dataset):
    def __init__(self, data_path):
        # In practice, load and preprocess your dataset here
        self.data = torch.load(data_path)  # assumes saved tensor dataset

    def __len__(self):
        return len(self.data["x"])

    def __getitem__(self, idx):
        return self.data["x"][idx], self.data["y"][idx]


def main():
    parser = argparse.ArgumentParser(description="Train a model with PyTorch Lightning")

    # Model parameters
    parser.add_argument("--model", type=str, required=True, help="Model name from models.py")
    parser.add_argument("--hidden_dim", type=int, default=128, help="Hidden dimension size")

    # Training parameters
    parser.add_argument("--train_data", type=str, required=True, help="Path to training data file")
    parser.add_argument("--val_data", type=str, required=True, help="Path to validation data file")
    parser.add_argument("--batch_size", type=int, default=32, help="Batch size")
    parser.add_argument("--epochs", type=int, default=10, help="Number of training epochs")
    parser.add_argument("--lr", type=float, default=1e-3, help="Learning rate")

    # Misc
    parser.add_argument("--gpus", type=int, default=0, help="Number of GPUs to use (0 for CPU)")
    parser.add_argument("--logdir", type=str, default="logs", help="Logging directory")

    args = parser.parse_args()

    # Load datasets
    train_dataset = SimpleDataset(args.train_data)
    val_dataset = SimpleDataset(args.val_data)

    train_loader = DataLoader(train_dataset, batch_size=args.batch_size, shuffle=True)
    val_loader = DataLoader(val_dataset, batch_size=args.batch_size)

    # Load model from models.py
    model = get_model(args.model, hidden_dim=args.hidden_dim, lr=args.lr)

    # Logger
    logger = TensorBoardLogger(save_dir=args.logdir, name=args.model)

    # Trainer
    trainer = pl.Trainer(
        max_epochs=args.epochs,
        accelerator="gpu" if args.gpus > 0 else "cpu",
        devices=args.gpus if args.gpus > 0 else None,
        logger=logger,
    )

    # Train
    trainer.fit(model, train_loader, val_loader)


if __name__ == "__main__":
    main()
```

------

### Example `models.py`

This would live alongside the script and define models you can import:

```python
# models.py
import pytorch_lightning as pl
import torch
from torch import nn
import torch.nn.functional as F


class SimpleMLP(pl.LightningModule):
    def __init__(self, input_dim=100, hidden_dim=128, lr=1e-3):
        super().__init__()
        self.save_hyperparameters()
        self.fc1 = nn.Linear(input_dim, hidden_dim)
        self.fc2 = nn.Linear(hidden_dim, 2)  # assume binary classification
        self.lr = lr

    def forward(self, x):
        x = F.relu(self.fc1(x))
        return self.fc2(x)

    def training_step(self, batch, batch_idx):
        x, y = batch
        logits = self(x)
        loss = F.cross_entropy(logits, y)
        self.log("train_loss", loss)
        return loss

    def validation_step(self, batch, batch_idx):
        x, y = batch
        logits = self(x)
        loss = F.cross_entropy(logits, y)
        acc = (logits.argmax(dim=1) == y).float().mean()
        self.log("val_loss", loss, prog_bar=True)
        self.log("val_acc", acc, prog_bar=True)

    def configure_optimizers(self):
        return torch.optim.Adam(self.parameters(), lr=self.lr)


def get_model(name: str, **kwargs):
    if name.lower() == "mlp":
        return SimpleMLP(**kwargs)
    else:
        raise ValueError(f"Unknown model: {name}")
```

------

✅ Example usage:

```bash
python model_training.py \
    --model mlp \
    --train_data train.pt \
    --val_data val.pt \
    --batch_size 64 \
    --epochs 20 \
    --lr 0.001 \
    --gpus 1
```