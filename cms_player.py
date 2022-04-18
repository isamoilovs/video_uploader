

def get_code_for_cms_player(class_id: str):
    cms_player_code = open('./output/' + class_id + '.txt', 'w')
    cms_player_code.write(
        """
<section class="reveal flex px-5 my-12 overflow-hidden">
    <div class="container mx-auto space-y-2">
        <div class="flex mx-auto">
            <h2 class="flex-grow font-accent text-lg">Начать """ + class_id + """ урок</h2>
        </div>
        <link
            rel="stylesheet"
            href="https://16402e8c-8037-46dd-8c51-bfd292a294ea.selcdn.net/player/s.min.css"
        />
        <div
          id="b-proplayer"
          data-mirror="0"
          data-wid="{uid}"
          data-double-video="1"
          data-video="https://16402e8c-8037-46dd-8c51-bfd292a294ea.selcdn.net/""" + class_id + """/media/""" + class_id + """.m3u8"
          data-poster="https://16402e8c-8037-46dd-8c51-bfd292a294ea.selcdn.net/site/img/covers/""" + class_id + """.jpg"
          data-thumbnails="https://16402e8c-8037-46dd-8c51-bfd292a294ea.selcdn.net/""" + class_id + """/vtt/""" + class_id + """.vtt"
          data-has-contents="1"
          data-contents="[{'sec':'160','time':'00:02:40','title':'ТЕСТОВЫЕ СУБТИТРЫ!!!'}]"
        ></div>

        <div class="socials_container">
            <h2 class="course-title">Музыка из урока</h2>
                <div class="socials">
                    <a href="https://vk.com/audio-2001485992_10485992_6c0f2dca6cc1762812" target="_blank" rel="noreferer" class="social">
                        <img
                          src="https://553502.selcdn.ru/videos/site/img/VK_Music_Logo_Main.png"
                          width="158"
                          height="32"
                        />
                    </a>
                    <a href="https://music.apple.com/ru/album/disco-inferno/1440879586?i=1440879602" target="_blank" rel="noreferer" class="social">
                        <img
                          src="https://553502.selcdn.ru/videos/site/img/itunes.png"
                          width="32"
                          height="32"
                        />
                    </a>
                    <a href="https://music.yandex.ru/album/4241614/track/767779" target="_blank" rel="noreferer" class="social">
                        <img
                          src="https://553502.selcdn.ru/videos/site/img/yandex.png"
                          width="32"
                          height="32"
                        />
                    </a>
                </div>
        </div>

        <script
            src="https://16402e8c-8037-46dd-8c51-bfd292a294ea.selcdn.net/player/p.js"
            type="text/javascript"
        ></script>
        <script>
            var waitForJQuery = setInterval(function () {
                "undefined" != typeof $ &&
                  ($.getScript(
                    "https://16402e8c-8037-46dd-8c51-bfd292a294ea.selcdn.net/player/s.min.js?2"
                    ),
                    clearInterval(waitForJQuery));
            }, 10);
        </script>
    </div>
</section>
        """
    )
    print("Скопируйте текст из файла " + class_id + '.txt и вставьте его в плеер!')
    print("Удостоверьтесь, что данные типа обложки, заголовков, таймкодов прописаны верно!")
