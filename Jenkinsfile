pipeline {
  agent any

  environment {
    DISPLAY = ":0"
    XDG_RUNTIME_DIR = "/run/user/123"
    PULSE_SERVER = "unix:/run/user/123/pulse/native"
  }

  stages {
    stage('📥 Checkout') {
      steps {
        echo "Checking out the repository..."
        checkout scm
      }
    }

    stage('🐳 Build Docker Image') {
      steps {
        echo "Building the Docker image..."
        sh '''
          docker build -t email-game -f docker/Dockerfile .
        '''
      }
    }

    stage('🕹️ Run the Game (GUI + Audio)') {
      steps {
        echo "Running the game container..."
        sh '''
          docker run --rm \
            --env DISPLAY=$DISPLAY \
            --env XDG_RUNTIME_DIR=$XDG_RUNTIME_DIR \
            --env PULSE_SERVER=$PULSE_SERVER \
            --env PULSE_LATENCY_MSEC=60 \
            --env SDL_AUDIODRIVER=alsa \
            --volume $XDG_RUNTIME_DIR:$XDG_RUNTIME_DIR \
            --volume /tmp/.X11-unix:/tmp/.X11-unix \
            --device /dev/snd \
            --group-add audio \
            email-game
        '''
      }
    }
  }

  post {
    always {
      echo "✅ Pipeline completed."
    }
    failure {
      echo "❌ Pipeline failed. Please check logs."
    }
  }
}
