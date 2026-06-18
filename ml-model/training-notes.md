# Training Notes

Workflow:

1. Collect attacker interaction logs
2. Store logs in Amazon S3
3. Preprocess behavioral data
4. Train model using SageMaker Studio
5. Export model artifacts
6. Store trained models in S3 (ml-models/)
7. Container Runtime retrieves trained model
8. Generate adaptive responses during inference

Integration:

SageMaker → S3 → Lambda Container Runtime
