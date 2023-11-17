import gspread
from gspread import Client, Spreadsheet, Worksheet


SPREADSHEET_URL = "https://docs.google.com/spreadsheets/d/1EBmb4VnhMi283oUBXxVKzSo-UGs2iC9tG0QqhEarwXg/edit#gid=1731395843"

#def show_available_worksheets(sh: Spreadsheet):
#    worksheets = sh.worksheets()

#    for ws in worksheets:
#        print("Worksheet with title", repr(ws.title), "and id", ws.id)


def main():
    gs: Client = gspread.service_account("./service_account.json")
    sh: Spreadsheet = gs.open_by_url(SPREADSHEET_URL)
    print(sh)
#    show_available_worksheets(sh)


if __name__ == '__main__':
    main()
