{{- define "monitoring.fullname" -}}
{{- printf "%s-%s" .Release.Name "monitoring" | trunc 63 | trimSuffix "-" -}}
{{- end -}}
