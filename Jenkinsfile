pipeline { 
 
    agent any 
 
    environment { 
 
        AWS_REGION = 'ap-south-1' 
 
        AWS_ACCOUNT_ID = 'YOUR_ACCOUNT_ID' 
 
        ECR_REGISTRY = 
            "${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com" 
 
        BACKEND_IMAGE = 
            "${ECR_REGISTRY}/shopflow-backend" 
 
        FRONTEND_IMAGE = 
            "${ECR_REGISTRY}/shopflow-frontend" 
    } 
 
    stages { 
 
        stage('Checkout') { 
            steps { 
                checkout scm 
            } 
        } 
 
        stage('Test Backend') { 
            steps { 
                sh 'python3 -m py_compile backend/app.py' 
            } 
        } 
 
        stage('Build Backend') { 
            steps { 
                sh ''' 
                    docker build \ 
                    -t ${BACKEND_IMAGE}:${BUILD_NUMBER} \ 
                    ./backend 
                ''' 
            } 
        } 
 
        stage('Build Frontend') { 
            steps { 
                sh ''' 
                    docker build \ 
                    -t ${FRONTEND_IMAGE}:${BUILD_NUMBER} \ 
                    ./frontend 
                ''' 
            } 
        } 
 
        stage('Login to ECR') { 
            steps { 
                sh ''' 
                    aws ecr get-login-password \ 
                    --region ${AWS_REGION} | \ 
                    docker login \ 
                    --username AWS \ 
                    --password-stdin ${ECR_REGISTRY} 
                ''' 
            } 
        } 
 
        stage('Push Backend') { 
            steps { 
                sh ''' 
                    docker push \ 
                    ${BACKEND_IMAGE}:${BUILD_NUMBER} 
                ''' 
            } 
        } 
 
        stage('Push Frontend') { 
            steps { 
                sh ''' 
                    docker push \ 
                    ${FRONTEND_IMAGE}:${BUILD_NUMBER} 
                ''' 
            } 
        } 
    } 
 
    post { 
        success { 
            echo 'ShopFlow CI/CD completed successfully!' 
        } 
 
        failure { 
            echo 'ShopFlow pipeline failed!' 
        } 
    } 
}
