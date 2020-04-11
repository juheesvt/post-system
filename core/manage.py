"""
db와 연동해주는 친구 우리는 모두친구
"""
import pickle


class ObjectManager:
    def __init__(self, file_name=None):
        self.file_name = file_name
        try:
            self.__objs = self.read()
        except:
            self.__objs = []

    def get_objs(self):
        return self.__objs

    def write(self, objs):
        with open(self.file_name, 'wb') as f:
            pickle.dump(objs, f)
        f.close()

    def read(self):
        with open(self.file_name, 'rb') as f:
            objs = pickle.load(f)
        f.close()
        return objs

    # search == 함수 => 검색에 걸리는 조건을 반환하는 함수
    def find(self, search_func):
        # TODO: for문으로 오브젝트들을 돌다가 search함수로 해당 오브젝트 넣었더니 true면 해당 오브젝트를 반환
        for obj in self.__objs:
            if search_func(obj):
                return obj
        return None

    def update(self, search_func, change_obj):
        for idx, obj in enumerate(self.__objs):
            if search_func(obj):
                self.__objs[idx] = obj
                self.write(self.__objs)
        return None

    def create(self, obj):
        obj.set_id(self.get_next_id())
        self.__objs.append(obj)
        self.write(self.__objs)
        return obj

    def get_next_id(self):
        return len(self.__objs) + 1
