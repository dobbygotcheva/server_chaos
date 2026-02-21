{{- define "mongodb.name" -}}
{{- default .Chart.Name .Values.nameOverride | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{- define "mongodb.fullname" -}}
{{- printf "%s-%s" .Release.Name (include "mongodb.name" .) | trunc 63 | trimSuffix "-" -}}
{{- end -}}
