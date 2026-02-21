{{- define "loadtest.fullname" -}}
{{- printf "%s-loadtest" .Release.Name | trunc 63 | trimSuffix "-" -}}
{{- end -}}
