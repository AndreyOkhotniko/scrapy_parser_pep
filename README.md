# Scrapy_parser_pep - асинхронный парсер PEP
## Описание проекта

Парсер документов PEP на базе фреймворка Scrapy, который выодит информацию в два файла .csv:
1. pep_(time) — список всех PEP: номер, название и статус.
2. status_summary_(time) — общая сводка по всем PEP.

## Инструкция по запуску 
1. Клонируйте репозиторий на свой компьютер: 
   ```bash 
   git clone https://github.com/AndreyOkhotniko/scrapy_parser_pep.git 
   ``` 
 
2. Перейдите в папку проекта: 
 
```  
cd scrapy_parser_pep 
```  
3. Cоздать и активировать виртуальное окружение, установить зависимости:  
  
```  
python3 -m venv env  
```  
  
```  
source env/bin/activate  
```  
```  
python3 -m pip install --upgrade pip 
```

```
pip install -r requirements.txt
```

### Запуск программы
```
scrapy crawl pep
```
Данные сохрянтся в дирректорию results

### Автор: 
[Охотников Андрей](https://github.com/AndreyOkhotniko)