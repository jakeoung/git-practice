import os
import time
import argparse

parser = argparse.ArgumentParser(add_help=False)
parser.add_argument('--tau', type=float, default=0.05, help='step size in curve evolution')
parser.add_argument('--N', type=int, default=200, help='number of points in a curve')
parser.add_argument('--K', type=int, default=30, help='number of angles')
parser.add_argument('--W', type=int, default=128, help='image width')
parser.add_argument('--alpha', type=float, default=0.5, help='length minimization parameter')
parser.add_argument('--beta', type=float, default=0.0, help='curvature minimization parameter')
parser.add_argument('--eta', type=float, default=0.05, help='noise std on the sinogram data')

args_key, unparsed = parser.parse_known_args()

def get_fresult(dic_):
    fresult_ = time.strftime('%m%d_')
    key_params = dic_.keys()
    for key in sorted(key_params):
        fresult_ += '--' + str(key) + '_' + str(dic_[key]) + '_'
    return fresult_

fresult = get_fresult(vars(args_key))

####################################
## Parsing secondary arguments
####################################
parser2 = argparse.ArgumentParser(parents=[parser], conflict_handler='resolve')

parser2.add_argument('--verbose', type=int, default=1, help='control verbose mode')
parser2.add_argument('--dataroot', type=str, default='../data/', help='data root')
parser2.add_argument('--dataset', type=str, default='makeheart', help='dataset name')
parser2.add_argument('--resroot', type=str, default='../result', help='result root')
args, unparsed = parser2.parse_known_args(namespace=args_key) # for jupyter
#args = parser2.parse_args(namespace=args_key) 

#####################################
### Directory structure example:
### args.dataroot: .../useg/data/dataset-name/
### args.dresult : .../useg/result/dataset-name/fckpt
###
### - .../useg/data/dataset-name/train/img1.png
### - .../useg/result/dataset-name/.../iter/...
#####################################
args.ddata = os.path.join(args.dataroot, args.dataset) + '/'
dresult = os.path.join(args.resroot, args.dataset) + '/' + fresult + '/'

#
#if os.path.exists(args.dresult):
#    if args.init:
#        import shutil
#        shutil.rmtree(args.dresult)
#        print('! Previous log is removed.')
#    else:
#        print('! RESTART')
