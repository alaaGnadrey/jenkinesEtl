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
                /*withPythonEnv('python') {
                   sh 'python --version'
                } */
                sh 'python -u sqlExecuter.py'      
            } 
        }
        stage('Cleaning') {
            steps {
                echo 'Cleaning....'
            }
        }
    }
}