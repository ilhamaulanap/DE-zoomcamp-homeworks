variable "gcp_project" {
  description = "The ID of your GCP project"
  type        = string
}

variable "gcp_region" {
  description = "The GCP region for resources"
  type        = string
}

variable "credentials" {
    description = "Credential for cloud provisioning"
    default = "credentials/key.json"
    type = string
}

variable "gcs_bucket_name" {
  description = "The name of the GCS bucket"
  type        = string
}

variable "gcs_bucket_location" {
  description = "The location of the GCS bucket"
  type        = string
}

variable "bigquery_dataset_id" {
  description = "BigQuery dataset"
  type        = string
}
