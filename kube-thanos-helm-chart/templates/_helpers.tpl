{{/* vim: set filetype=mustache: */}}

{{- define "thanos.fullname" -}}
  {{- if .Values.global.fullNameoverride -}}
    {{- .Values.global.fullNameOverride -}}
  {{- else -}}
    {{- .Release.Name -}}
  {{- end -}}
{{- end -}}


{{- define "thanos.commonlabels" -}}
helm.sh/chart: {{ include "thanos.fullname" . }}
{{ include "thanos.selectorlabels" . }}
{{- if .Chart.AppVersion }}
app.kubernetes.io/version: {{ .Chart.AppVersion | quote }}
{{- end }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
{{- end }}

{{- define "thanos.selectorlabels" -}}
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end }}


