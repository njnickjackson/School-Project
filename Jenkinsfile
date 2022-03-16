pipeline {
  agent {
    kubernetes {
      yamlFile 'KubernetesBuilder.yaml'
    }
  }
  stages {
    stage('Build') {
      steps {
        checkout scm
        container('python') {
          sh 'cargo build --release'
        }
      }
    }
    stage('Copy Artifacts') {
      steps {
        container('python') {
          sh 'cp -r * /workspace/opt/app/shared/'
        }
      }
    }
    stage('Release') {
      steps {
        checkout scm
        container('kaniko') {
          sh 'cp -r /workspace/opt/app/shared/*  /workspace'
          sh 'ulimit -n 10000'
          sh '/kaniko/executor -f Dockerfile --destination=docker.ultimaengineering.io/student-project-api:${BRANCH_NAME}-${BUILD_NUMBER} --destination=docker.ultimaengineering.io/student-project-api:latest'
        }
      }
    }
  }
}