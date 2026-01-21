ui = true

listener "tcp" {
  address     = "0.0.0.0:8200"
  tls_disable = "true"        # TLS는 Nginx 에서 처리
}

#api_addr = "https://vault.emro.co.kr:8200"
api_addr = "http://localhost:8200"

storage "file" {
  path = "/vault/file"
}

disable_mlock = true
