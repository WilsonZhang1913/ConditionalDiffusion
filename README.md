# This repo is based on https://github.com/IGITUGraz/WeatherDiffusion with modification 


## Datasets

We perform experiments for raindrop removal on
the [RainDrop](https://github.com/rui1996/DeRaindrop) datasets. 

## To train the model

python train_diffusion.py --config "allweather.yml" --resume 'WeatherDiff1024.pth.tar' --sampling_timesteps 25

## To evaluate the model 

python eval_diffusion.py --config "allweather_test.yml" --resume 'patch_ddpm_14000.pth.tar' --test_set 'snow' --sampling_timesteps 25


