
class Net(torch.nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.bn_input = torch.nn.BatchNorm1d(384, momentum=0.8)   
        self.conv1 = nn.Sequential(       
            nn.Conv1d(
                in_channels=1,
                out_channels=30,
                kernel_size=1,
                stride=1,
                padding=0),         
            nn.ReLU(),
            nn.MaxPool1d(kernel_size=2))   
        self.conv2 = nn.Sequential(
            nn.Conv1d(
                in_channels=30,
                out_channels=1,
                kernel_size=1,
                stride=1,
                padding=0),   
            nn.ReLU(),
            nn.MaxPool1d(kernel_size=2))   
            
        self.encoder = nn.Sequential(        
            nn.Linear(96, 64),
            nn.BatchNorm1d(64, momentum=0.5),
            # nn.Dropout(0.5),
            nn.LeakyReLU(inplace=True),
            nn.Linear(64, 48))             
        
        for p in self.parameters():
            p.requires_grad = False
            
        self.rnn1 = nn.Sequential(          
            nn.LSTM(
            input_size = 48,
            hidden_size = 32,
            num_layers = 3,
            batch_first = True))
            
        self.decoder = nn.Sequential(
            nn.Linear(32, 16),
#             nn.BatchNorm1d(16, momentum=0.5),
#             nn.Dropout(0.5),
            nn.LeakyReLU(inplace=True),
            nn.Linear(16, 8),
#             nn.BatchNorm1d(8, momentum=0.5),
#             nn.Dropout(0.5),
            nn.LeakyReLU(inplace=True),
            nn.Linear(8, 1),
        )
