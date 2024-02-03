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
