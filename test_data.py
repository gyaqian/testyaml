# _*_ coding:utf-8 _*_
import yaml
import pytest


datas = yaml.safe_load(open('./data.yaml'))
print(datas)

class TestDemo():
    @pytest.mark.parametrize('env', datas)
    def test_demo(self,env):
        if 'test' in env:
            print("这是测试环境")
            print(env["test"])

        elif 'Dev' in env:
            print("这是开发环境")
            print(env["Dev"])
    assert 1 == 1

if __name__ == '__main__':
    pytest.main(['test_data.py'])