

from tldextract import tldextract


# 获取带域名的链接
class GetDomainUrl(object):
    def __init__(self):
        self.tld = tldextract
        self.target_domain = None

    def get_domain_url(self, url):
        domain_val = self.tld.extract(url)
        suffix = domain_val.suffix
        suffix_index = url.index(suffix)
        suffix_length = len(suffix)
        domain_url = url[:suffix_index + suffix_length]
        # print(url[:suffix_index + suffix_length])
        return domain_url if domain_url else None



    def set_allowed_domains(self, url):
        domain_val = self.tld.extract(url)
        # if domain_val.domain == self.target_domain:
        domains = "{}.{}.{}".format(domain_val.subdomain, domain_val.domain, domain_val.suffix)
        print(domains)
        # self.domains_set.add(domains)

    def get_allowed_domains(self, start_url_or_domain):
        domain_val = self.tld.extract(start_url_or_domain)
        self.target_domain = domain_val.domain
        domains = "{}.{}".format(domain_val.domain, domain_val.suffix)
        return domains


if __name__ == '__main__':
    gdu = GetDomainUrl()
    res = gdu.get_domain_url("//n.sinaimg.cn/spider20191210/317/w653h464/20191210/20e1-iknhexi5450926.jpg")
    # res = gdu.set_allowed_domains("//n.sinaimg.cn/spider20191210/317/w653h464/20191210/20e1-iknhexi5450926.jpg")
    # res = gdu.get_allowed_domains("//n.sinaimg.cn/spider20191210/317/w653h464/20191210/20e1-iknhexi5450926.jpg")
    # print(res)
