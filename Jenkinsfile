pipeline {
    agent any
    environment {
        AWS_REGION = 'eu-central-1'
        ECR_REPO = 'cloud-gallery-repo'
        IMAGE_TAG = 'latest'
    }
    stages {
        stage('Authenticate AWS CLI') {
            steps {
                withCredentials([
                    string(credentialsId: 'AWS_ACCESS_KEY_ID', variable: 'AWS_ACCESS_KEY_ID'),
                    string(credentialsId: 'AWS_SECRET_ACCESS_KEY', variable: 'AWS_SECRET_ACCESS_KEY')
                ]) {
                    sh '''
                    $(which aws) configure set aws_access_key_id $AWS_ACCESS_KEY_ID
                    $(which aws) configure set aws_secret_access_key $AWS_SECRET_ACCESS_KEY
                    $(which aws) configure set region $AWS_REGION
                    '''
                }
            }
        }
        stage('Build Docker Image') {
            steps {
                withCredentials([
                    string(credentialsId: 'AWS_ACCOUNT_ID', variable: 'AWS_ACCOUNT_ID'),
                ]) {
                    sh '$(which docker) build -t cloud-gallery .'
                    sh "$(which docker) tag $ECR_REPO:$IMAGE_TAG $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$ECR_REPO:$IMAGE_TAG"
                }
            }
        }
        stage('Push Docker Image to ECR') {
            steps {
                withCredentials([
                    string(credentialsId: 'AWS_ACCOUNT_ID', variable: 'AWS_ACCOUNT_ID'),
                ]) {
                    sh "$(which docker) push $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$ECR_REPO:$IMAGE_TAG"
                }
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
