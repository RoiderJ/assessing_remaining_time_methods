import torch
from torch_geometric.graphgym import cfg
from torch_geometric.graphgym.register import register_edge_encoder


@register_edge_encoder('TwoLayerLinearEdge')
class TwoLayerLinearEdgeEncoder(torch.nn.Module):
    def __init__(self, emb_dim):
        super().__init__()
        """
        if cfg.dataset.name in ['BPIC12CWcycletimeprediction' , 'BPIC12Ocycletimeprediction',
                                  'BPIC12Wcycletimeprediction']:
            self.in_dim = 68 
        elif cfg.dataset.name in ['BPIC12cycletimeprediction' , 'BPIC12Ccycletimeprediction']:
            self.in_dim = 77
        elif cfg.dataset.name == 'BPIC12Acycletimeprediction':
            self.in_dim = 69
        elif cfg.dataset.name == 'BPIC13Ccycletimeprediction':
            self.in_dim = 93          
        elif cfg.dataset.name == 'BPIC13Icycletimeprediction':
            self.in_dim = 115
        elif cfg.dataset.name == 'BPIC20Dcycletimeprediction':
            self.in_dim = 17
        elif cfg.dataset.name == 'BPIC20Icycletimeprediction':
            self.in_dim = 407
        elif cfg.dataset.name == 'ENVPERMITcycletimeprediction':
            self.in_dim = 120
        elif cfg.dataset.name == 'HELPDESKcycletimeprediction':
            self.in_dim = 477
        elif cfg.dataset.name == 'HOSPITALcycletimeprediction':
            self.in_dim = 150
        elif cfg.dataset.name == 'SEPSIScycletimeprediction':
            self.in_dim = 250
        elif cfg.dataset.name == 'Trafficfinescycletimeprediction':
            self.in_dim = 267
        elif cfg.dataset.name == 'BPIC15M1cycletimeprediction':
            self.in_dim = 219 
        elif cfg.dataset.name == 'BPIC15M2cycletimeprediction':
            self.in_dim = 142 
        elif cfg.dataset.name == 'BPIC15M3cycletimeprediction':
            self.in_dim = 209 
        elif cfg.dataset.name == 'BPIC15M4cycletimeprediction':
            self.in_dim = 141
        elif cfg.dataset.name == 'BPIC15M5cycletimeprediction':
            self.in_dim = 208 
        # extra condition for ablation study:
        elif 'ablation' in cfg.dataset.name:
            self.in_dim = 6 
        else:
            raise ValueError("Input edge feature dim is required to be hardset "
                             "or refactored to use a cfg option.")
        """
        self.in_dim = int(cfg.two_layer_linear_edge_encoder.in_dim)
            
        self.encoder1 = torch.nn.Linear(self.in_dim, int((emb_dim+self.in_dim)/2))
        self.encoder2 = torch.nn.Linear(int((emb_dim+self.in_dim)/2), emb_dim)

    def forward(self, batch):
        batch.edge_attr = self.encoder1(batch.edge_attr.view(-1, self.in_dim))
        batch.edge_attr = self.encoder2(batch.edge_attr)
        return batch