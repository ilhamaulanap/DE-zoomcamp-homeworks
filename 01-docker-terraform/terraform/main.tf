provider "google" {
  credentials = var.credentials #use credentials if run locally
  project     = var.gcp_project
  region      = var.gcp_region
}

# Create a GCS buckets
resource "google_storage_bucket" "my_bucket" {
  name          = var.gcs_bucket_name
  location      = var.gcs_bucket_location
  force_destroy = true
}

# Create a bigquery dataset
resource "google_bigquery_dataset" "my_dataset" {
  dataset_id = var.bigquery_dataset_id
  project    = var.gcp_project
  delete_contents_on_destroy = true

  labels = {
    environment = "homework"
  }
}
