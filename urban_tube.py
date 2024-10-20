class User:

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return self.nickname

class Video:

    def __init__(self, title, duration, time_now=0, adult_mode = False):
        self.title = title
        self.duration = int(duration)
        self.time_now = int(time_now)
        self.adult_mode = int(adult_mode)

    def __eq__(self, other):
        if self.title == other.title:
            return True
        return False
class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        for i in self.users:
            if i.nickname == nickname and hash(i.password) == password:
                self.current_user = i
        return self

    def register(self, nickname, password, age):
        for i in self.users:
            if i.nickname == nickname:
                print(f'Пользователь {nickname} уже существует')
                return self
        tmp = User(nickname, password, age)
        self.users.append(tmp)
        self.current_user = tmp
        del tmp
        return self

    def log_out(self):
        self.current_user = None

    def add(self, *Videos):
        for i in Videos:
            if i not in self.videos:
                self.videos.append(i)
        return self

    def get_videos(self, key):
        key = key.lower()
        tmp = []
        for i in self.videos:
            if key in i.title.lower():
                tmp.append(i.title)
        return tmp

    def watch_video(self, title):
        if self.current_user != None:
            for i in self.videos:
                if title in i.title:
                    if self.current_user.age >= int(i.adult_mode) * 18:
                        from time import sleep
                        for a in range(i.time_now, i.duration + 1):
                            sleep(1)
                            if a != i.time_now:
                                print(a, end=" ")
                        print("Конец видео")
                        return self
                    self.error("adult_error")
                    return self
            self.error("video not found")
            return self
        self.error("logged_error")

    def error(self, error):
        nutifications = {
            "logged_error": "Войдите в аккаунт, чтобы смотреть видео",
            "adult_error": "Вам нет 18 лет, пожалуйста покиньте страницу",
            "video not found": "Видео не существует"
        }
        print(nutifications.get(error))

if __name__=="__main__":
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео
    ur.add(v1, v2)

    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)

    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')



