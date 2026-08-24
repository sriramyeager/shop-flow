pipeline {

    agent any

    environment {
        AWS_REGION = 'ap-south-1'
        AWS_ACCOUNT_ID = '545931886446'
        ECR_REGISTRY = "${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com"

        BACKEND_IMAGE = "${ECR_REGISTRY}/shopflow-backend"
        FRONTEND_IMAGE = "${ECR_REGISTRY}/shopflow-frontend"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Test Backend') {
            steps {
                sh '''
                    python3 -m py_compile backend/app.py
                '''
            }
        }

        stage('Build Backend') {
            steps {
                sh '''
                    docker build -t shopflow-backend:latest ./backend
                '''
            }
        }

        stage('Build Frontend') {
            steps {
                sh '''
                    docker build -t shopflow-frontend:latest ./frontend
                '''
            }
        }

        stage('Login to ECR') {
            steps {
                sh '''
                    aws ecr get-login-password --region ${AWS_REGION} | \
                    docker login --username AWS --password-stdin ${ECR_REGISTRY}
                '''
            }
        }

        stage('Tag Images') {
            steps {
                sh '''
                    docker tag shopflow-backend:latest ${BACKEND_IMAGE}:latest
                    docker tag shopflow-frontend:latest ${FRONTEND_IMAGE}:latest
                '''
            }
        }

        stage('Push Backend') {
            steps {
                sh '''
                    docker push ${BACKEND_IMAGE}:latest
                '''
            }
        }

        stage('Push Frontend') {
            steps {
                sh '''
                    docker push ${FRONTEND_IMAGE}:latest
                '''
            }
        }
    }

    post {
        success {
            echo 'ShopFlow pipeline completed successfully!'
        }

        failure {
            echo 'ShopFlow pipeline failed!'
        }
    }
}
