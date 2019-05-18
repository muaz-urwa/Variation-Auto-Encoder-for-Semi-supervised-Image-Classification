batch_size   = 150

config = {}
# set the parameters related to the training and testing set
data_train_opt = {} 
data_train_opt['batch_size'] = batch_size
data_train_opt['unsupervised'] = False
data_train_opt['epoch_size'] = None
data_train_opt['random_sized_crop'] = False
data_train_opt['dataset_name'] = 'custom'
data_train_opt['split'] = 'supervised/train'

data_test_opt = {}
data_test_opt['batch_size'] = batch_size
data_test_opt['unsupervised'] = False
data_test_opt['epoch_size'] = None
data_test_opt['random_sized_crop'] = False
data_test_opt['dataset_name'] = 'custom'
data_test_opt['split'] = 'supervised/val'

config['data_train_opt'] = data_train_opt
config['data_test_opt']  = data_test_opt
config['max_num_epochs'] = 40


networks = {}

pretrained = './vaeSiam.pth.tar'
networks['feat_extractor'] = {'def_file': 'architectures/vaecnn.py', 'pretrained': pretrained, 'opt': {'num_classes': 4},  'optim_params': None} 

# net_opt_cls = [None] * 2
# net_opt_cls[0] = {'cls_type':'Alexnet_conv4', 'nChannels':256, 'num_classes':1000}
# net_opt_cls[1] = {'cls_type':'Alexnet_conv5', 'nChannels':256, 'num_classes':1000}
# out_feat_keys = ['conv4', 'conv5']

net_opt_cls = [None] * 1
#net_opt_cls[0] = {'cls_type':'Alexnet_conv4', 'nChannels':256, 'num_classes':1000}
net_opt_cls[0] = {'cls_type':'Vae', 'nChannels':256, 'num_classes':1000}
out_feat_keys = ['conv5']


net_optim_params_cls = {'optim_type': 'sgd', 'lr': 0.1, 'momentum':0.9, 'weight_decay': 5e-4, 'nesterov': True, 'LUT_lr':[(10, 0.01),(20, 0.002),(30, 0.0004),(40, 0.00008)]}
networks['classifier']  = {'def_file': 'architectures/MultipleNonLinearClassifiers.py', 'pretrained': None, 'opt': net_opt_cls, 'optim_params': net_optim_params_cls}

config['networks'] = networks

criterions = {}
criterions['loss'] = {'ctype':'CrossEntropyLoss', 'opt':None}
config['criterions'] = criterions
config['algorithm_type'] = 'FeatureClassificationModel'
config['out_feat_keys'] = out_feat_keys
