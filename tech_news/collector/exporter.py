from tech_news import database
import csv


def csv_exporter(filepath):
    if not filepath.endswith(".csv"):
        raise ValueError("Formato invalido")

    news = database.find_news()

    try:
        with open(filepath, "w", newline="") as file:
            writer = csv.writer(file, delimiter=";")
            headers = [
                "url",
                "title",
                "timestamp",
                "writer",
                "shares_count",
                "comments_count",
                "summary",
                "sources",
                "categories",
            ]
            writer.writerow(headers)
            row = []
            for index, item in enumerate(headers):
                if type(news[0][item]) == list:
                    print("inside if")
                    my_list = news[0][item]
                    my_string = ','.join(my_list)
                    row.append(my_string)
                else:
                    row.append(news[0][item])
            writer.writerow(row)
    except:
        print("cvs export went wrong")

    else:
        print("arquivo manipulado e fechado com sucesso")
        file.close()
