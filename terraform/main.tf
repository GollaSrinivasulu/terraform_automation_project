terraform {
  required_providers {
    null = {
      source = "hashicorp/null"
    }
    local = {
      source = "hashicorp/local"
    }
  }
}

provider "null" {}
provider "local" {}

# Build Docker image
resource "null_resource" "docker_build" {
  provisioner "local-exec" {
    command = "docker build -t bayer_pipeline .."
  }
}

# Run Spark container
resource "null_resource" "docker_run" {
  depends_on = [null_resource.docker_build]

  provisioner "local-exec" {
    command = "docker rm -f bayer_spark_run || true && docker run --name bayer_spark_run bayer_pipeline"
  }
}


# Copy output file from container to host
resource "null_resource" "copy_output" {
  depends_on = [null_resource.docker_run]

  provisioner "local-exec" {
    command = "docker cp bayer_spark_run:/opt/app/cleaned_data.csv ../cleaned_data.csv"
  }
}

# Confirmation file
resource "local_file" "infra_ready" {
  filename   = "${path.cwd}/infra_ready.txt"
  content    = "Terraform executed Spark Docker pipeline successfully."
  depends_on = [null_resource.copy_output]
}
