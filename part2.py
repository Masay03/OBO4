# from abc import ABC, abstractmethod
#
# class Formatter(ABC):
#     @abstractmethod
#     def format(self, report):
#         pass
#
# class TextFormatter(Formatter):
#     def format(self, report):
#         print(report.title)
#         print(report.content)
#         print()
#
# class HTMLFormatter(Formatter):
#     def format(self, report):
#         print(f"<h1>{report.title}</h1>")
#         print(f"<p>{report.content}</p>")
#         print()
#
# class Report:
#     def __init__(self, title, content, formatter):
#         self.title = title
#         self.content = content
#         self.formatter = formatter
#
#     def docPrint(self):
#         self.formatter.format(self)
#
# report = Report('Заголовок отчёта','Содержание отчёта', TextFormatter()) # или HTMLFormatter()
# report.formatter.format(report)
