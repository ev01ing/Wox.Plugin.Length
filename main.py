# coding:utf-8
from wox import Wox, WoxAPI
import sys

if sys.version[0] == "2":
    reload(sys)
    sys.setdefaultencoding("utf-8")


class Main(Wox):

    def query(self, key):
        results = []

        if not key:
            self._construct_result("请输入", None, results)
        else:
            self._construct_result(len(key), "长度", results)

        return results

    @classmethod
    def _construct_result(cls, title, subtitle, results):
        results.append({
            "Title": title,
            "SubTitle": subtitle,
            "IcoPath": "images/icon.png",
        })


if __name__ == "__main__":
    Main()
