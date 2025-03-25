pipeline {
    agent any
    environment {
        AWS_REGION = 'eu-central-1'
        ECR_REPO = 'cloud-gallery-repo'
        IMAGE_TAG = "latest"
    }
    stages {
        stage('Authenticate AWS CLI') {
            steps {
                withCredentials([
                    string(credentialsId: 'AWS_ACCESS_KEY_ID', variable: 'AWS_ACCESS_KEY_ID'),
                    string(credentialsId: 'AWS_SECRET_ACCESS_KEY', variable: 'AWS_SECRET_ACCESS_KEY')
                ]) {
                    sh '''
                    aws configure set aws_access_key_id $AWS_ACCESS_KEY_ID
                    aws configure set aws_secret_access_key $AWS_SECRET_ACCESS_KEY
                    aws configure set region $AWS_REGION
                    '''
                }
            }
        }
        stage('Build') {
            steps {
                withCredentials([
                    string(credentialsId: 'AWS_ACCOUNT_ID', variable: 'AWS_ACCOUNT_ID'),
                ]) {
                    sh 'docker build -t cloud-gallery .'
                    sh "docker tag $ECR_REPO:$IMAGE_TAG $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$ECR_REPO:$IMAGE_TAG"
                }
            }
        }
        stage('Deploy') {
            steps {
                sh 'echo Deploying to production...'
            }
        }
    }
    post {
        always {
            echo 'Pipeline finished'
        }
        success {
            echo 'Build succeeded!'
        }
        failure {
            echo 'Build failed!'
        }
    }
}
