pipeline {
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
            echo 'Executing..'
            stages{
                stage('execute_step1'){
                    steps {
                        withPythonEnv('python') {
                            sh 'python -u -m resources.pipelines.poc_pipeline.execute_step2'   
                        }
                    }    
                }
                stage('execute_step2'){
                    steps {                        
                        withPythonEnv('python') {
                            sh 'python -u -m resources.pipelines.poc_pipeline.execute_step2'   
                        }
                    }    
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