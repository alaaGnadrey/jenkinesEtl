pipeline {
    timestamp{
    agent any

    stages {
        stage('Prepare') {
            steps {
                withPythonEnv('python') {
                    // Creates the virtualenv before proceeding
                    echo 'install requirements..'
                    sh 'pip install -r resources/requirements.txt'    
                }
            }
        }
        stage('Execute') {
            steps {
                echo 'Executing..'
                withPythonEnv('python') {
                   sh 'python -u -m resources.executors.sql_executer'      
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
}