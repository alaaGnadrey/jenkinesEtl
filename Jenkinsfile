pipeline {
    agent any

    stages {
        stage('Prepare') {
            steps {
                echo 'Preparing..'
            }
        }
        stage('Execute') {
            steps {
                echo 'Executing..'
                python {
                   command('python sqlExecuter.py')
                }   
            } 
        }
        stage('Cleaning') {
            steps {
                echo 'Cleaning....'
            }
        }
    }
}