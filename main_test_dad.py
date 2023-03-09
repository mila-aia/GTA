import torch
from models.gta import GraphTemporalEmbedding

if __name__ == '__main__':

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    x = torch.randn(32, 96, 122).to(device=device)
    # num_nodes, seq_len, num_levels
    model = GraphTemporalEmbedding(122, 96, 3).to(device=device)
    y = model(x)
    print(y.size())
