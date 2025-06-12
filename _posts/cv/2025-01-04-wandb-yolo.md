---
title: "[CV] YOLOv8 % WanDB sweep으로 파인튜닝 최적화"
date: 2025-01-04 18:24:28 +0900
categories: cv
tags: cv yolo wandb mlops
header:
  teaser: "../../img/cover/cv_logo.png"
---

AI 모델을 학습 시킬 때, WanDB를 이용하여 하이퍼파라미터를 쉽게 최적화할 수 있다.

### WanDB란?
- Wandb는 ML/AI 모델 학습 시, 학습 상황을 tracking(추적) 하여 진행이 잘 되고 있는지 확인할 수 있는 툴
- 또한, 여러 하이퍼파라미터 조합으로 학습을 시도하여 최적의 하이퍼파라미터를 찾아내도록 돕는 툴
학습 결과를 기록하고 관리하여 성능 개선을 돕는 툴
 

### wandb와 yolov8 (ultralytics) 모델 함께 사용하기

```python
import wandb
wandb.login()

from ultralytics import YOLO
import ultralytics
from wandb.integration.ultralytics import add_wandb_callback
```

- wandb.login() -> wandb 사이트에서 API 확인 -> 입력
 

```python
wandb.init(project='sample_project', job_type='training')
```

- wandb.init() 으로 어떤 프로젝트인지, 어떤 작업으로 wandb를 동작하게 할건지 설정
 

```python
sweep_config = {
    'method': 'random',
    'metric': {'goal': 'maximize', 'name': 'metrics/mAP50(B)'},
    'parameters': {
        'batch_size': {
            'values': [16, 32, 64]
        },
        'learning_rate': {
            'distribution': 'uniform',
            'min':0.0001,
            'max':0.001
        } 
    }
}
```

- 내가 하고 싶은 건 'sweep' 이므로 sweep_config를 설정
- sweep은 한 모델만의 학습을 wandb로 모니터링하는 게아니라, 여러 하이퍼파라미터들을 바꿔가며 알아서 여러번 학습하고, 그 결과를 저장/비교할 수 있도록 한 것

![](/img/2025-01-04/0104-1.PNG)

- learning rate decay, category, learning rate 라는 초매개 변수들의 여러 조합을 변화시키면서 학습할 때,
- 각 학습의 결과 Accuracy가 가장 높은 조합은 무엇인지 찾아낼 수 있음
 

- 내 config 에서는 batch_size와 learning_rate만 조절
 

```python
sweep_id = wandb.sweep(sweep=sweep_config, project='sds')
def yolo_train():
    with wandb.init() as run:
        config = wandb.config

        # 모델 정의 및 하이퍼파라미터 사용
        model = YOLO('yolov8n.pt')
        add_wandb_callback(model, enable_model_checkpointing=True)
        results = model.train(data='/data/sds/datasets/version_1/data.yaml', name='version_1_',
                              plots=True, batch=config.batch_size, epochs=10, imgsz=640,
                              cos_lr=True, lrf=0.01, lr0=config.learning_rate)
        wandb.log({
            'epoch': epoch, 
            'val_loss': val/dfl_loss
        })
```


- 자동으로 매번 학습을 시도할 함수를 정의해줌
- batch=config.batch_size 처럼 변화를 주면서 학습시킬 변수를 설정해놓음
- 나중에 학습 과정에서 로그를 남기고 싶은 값은 wandb.log로 설정해놓음 
 

```python
wandb.agent(sweep_id, function=yolo_train)
```

![](/img/2025-01-04/0104-2.PNG)


- 이제 wandb.agent로 알아서 yolo_train이라는 함수를 사용해서 학습을 시켜라 라고 지정해놓으면 끝
 


 

 

왼쪽 탭에 sweep들 (파라미터 조합을 여러가지로 시도해서 학습하고 있는 각 모델 경우의 수)로

알아서 agent가 잘 학습하고 있는 것을 보여준다. 이제 학습이 끝나고 가장 mAP가 높았던 파라미터를 최적으로 선정하면 끝!