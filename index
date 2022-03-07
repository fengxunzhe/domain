#python AD网走脚本访问外网内域模块pypac
#第一种: 使用pypac调用本地自动代理的文件pac格式
从 pypac 导入 PACSession，get_pac 
...
  pac = get_pac(url='http://10.18.88.118/proxy.pac')
  st = PACSession(pac)
  result = st.get('http://www.baidu.com')
  print(result.text)
...
#第二种:查看文件pac走的代理地址：PAC文件

                    function FindProxyForURL(url, host)
                    {
                        if (dnsDomainIs(host, ".bis.doc.gov")||
                            dnsDomainIs(host, "udemy.com")||
                            dnsDomainIs(host, "ssl.gstatic.com")||
                            dnsDomainIs(host, ".gstatic.com")||
                            dnsDomainIs(host, ".googleapis.com")||
                            dnsDomainIs(host, ".googleusercontent.com")||
                            dnsDomainIs(host, "raw.githubusercontent.com")||
                            dnsDomainIs(host, "ssl.google-analytics.com")||
                            dnsDomainIs(host, "members.jedec.org")||
                            dnsDomainIs(host, "code.jquery.com")||
                            dnsDomainIs(host, "use.fonticons.com")||
                            dnsDomainIs(host, "employeeinsight.mercer.com")
                             )
                      {
                      return "PROXY 10.219.45.15:8080";
                      }
                        if (shExpMatch(host, "sangfor5-9804.ymtc.local")||
                          shExpMatch(host, "sangfor5-be5b.ymtc.local")||
                        isInNet(host, "10.0.0.0", "255.0.0.0")||
                              isInNet(host, "172.16.0.0", "255.240.0.0")||
                                    isInNet(host, "116.211.59.251", "255.255.255.255")||
                                    isInNet(host, "211.91.168.149", "255.255.255.255")||
                                    isInNet(host, "208.185.171.167", "255.255.255.255")||
                                    isInNet(host, "12.235.168.101", "255.255.255.255")||
                                    isInNet(host, "127.0.0.0", "255.0.0.0"))
                      {
                      return "DIRECT";
                      }
                        else if (isInNet(myIpAddress(), "10.216.0.0", "255.255.0.0")|| 
                        isInNet(myIpAddress(), "10.224.0.0", "255.255.0.0"))

                      {
                      return "PROXY 10.216.112.191:8080";
                      }
                        else if (isInNet(myIpAddress(), "10.16.0.0", "255.240.0.0")||    
                                     isInNet(myIpAddress(), "10.32.0.0", "255.224.0.0")||
                         isInNet(myIpAddress(), "10.64.0.0", "255.192.0.0")||
                         isInNet(myIpAddress(), "10.128.0.0", "255.240.0.0")||
                                     isInNet(myIpAddress(), "10.218.0.0", "255.255.0.0")||
                         isInNet(myIpAddress(), "172.21.0.0", "255.255.0.0")||
                                     isInNet(myIpAddress(), "172.31.0.0", "255.255.254.0")||
                         isInNet(myIpAddress(), "172.22.0.0", "255.255.0.0")||
                         isInNet(myIpAddress(), "172.23.0.0", "255.255.0.0")||
                         isInNet(myIpAddress(), "192.168.0.0", "255.255.0.0")||
                        isInNet(myIpAddress(), "10.240.0.0", "255.255.0.0")||
                        isInNet(myIpAddress(), "10.221.0.0", "255.255.0.0"))
                        {
                          return "PROXY 172.21.1.30:8080";
                      }
此处找到代理地址： return "PROXY 172.21.1.30:8080";然后按正常走proxy="http://172.21.1.30:8080"
即可正常访问外网

#########################################################################################################分割线##############################################################


# python  AD域下爬取内网
response = requests.get(website_url, auth=HttpNtlmAuth('domain\\user', 'pwd'))
print(response.text)


# 证书错误  这里是由于这个网页的证书没有被官方CA机构信任，所以这里会出现证书验证的错误   证书校验 false  verify=False
# requests.exceptions.SSLError: HTTPSConnectionPool(host='www.pearvideo.com', port=443): Max retries exceeded with url: /videoStatus.jsp?contId=1750709&mrd=0.30104970988192226 (Caused by SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self signed certificate in certificate chain (_ssl.c:1056)')))

r = requests.get('https://www.12306.cn', verify=False)

# 安全警告  忽略    logging.captureWarnings(True)
C:\Program Files\Python37\lib\site-packages\urllib3\connectionpool.py:1020: InsecureRequestWarning: Unverified HTTPS request is being made to host '172.21.1.30'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/1.26.x/advanced-usage.html#ssl-warnings
  InsecureRequestWarning,
  
  logging.captureWarnings(True)
