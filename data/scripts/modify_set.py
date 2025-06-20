import csv
import sys

players = {"An Se Young": 1, "Anders ANTONSEN": 2, "Anthony Sinisuka GINTING": 3, "Busanan ONGBAMRUNGPHAN": 4, "Carolina MARIN": 5, 
           "CHEN Long": 6, "CHOU Tien Chen": 7, "Evgeniya KOSETSKAYA": 8, "Hans-Kristian Solberg VITTINGHUS": 9, "Jonatan CHRISTIE": 10,
           "Kento MOMOTA": 11, "KIDAMBI Srikanth": 12, "LEE Cheuk Yiu": 13, "LEE Zii Jia": 14, "LIEW Daren": 15, 
           "Mia BLICHFELDT": 16, "Michelle LI": 17, "Neslihan YIGIT": 18, "NG Ka Long Angus": 19, "Pornpawee CHOCHUWONG": 20,
           "PUSARLA V. Sindhu": 21, "Rasmus GEMKE": 22, "Ratchanok INTANON":23, "Sameer VERMA": 24, "SHI Yuqi": 25,
           "Supanida KATETHONG": 26, "Viktor AXELSEN": 27}
shot_types = { "放小球": "net shot", "擋小球": "return net", "殺球": "smash", "點扣": "wrist smash", "挑球": "lob",	
               "防守回挑": "defensive return lob", "長球": "clear", "平球": "drive", "小平球": "driven flight",
               "後場抽平球": "back-court drive", "切球": "drop", "過度切球": "passive drop", "推球": "push",
               "撲球": "rush", "防守回抽": "defensive return drive", "勾球": "cross-court net shot", "發短球": "short service", 
               "發長球": "long service", "未知球種": "unknown"}
reasons = {"落地致勝": "Shuttle Landing", "對手落地致勝": "Opponent Shuttle Landing",  "對手掛網": "Opponent Hanging Net", "掛網": "Hanging Net", 
           "出界": "Well Wide","對手出界": "Opponent Well Wide", "未過網": "Net Error", "對手未過網": "Opponent Net Error", 
           "落點判斷失誤": "Shuttle Location Judgement Error", "對手落點判斷失誤": "Opponent Shuttle Location Judgement Error", "犯規": "Penalty", "對手犯規": "Opponent Penalty",
           "對手落地判斷失誤": "Opponent Location Judgement Error",  "落地判斷失誤": "Location Judgement Error",}

matches = {
    '1': [11, 7], '2': [6, 7], '3': [11, 7], '4': [6, 7], '5': [11, 7], '6': [11, 7], '7': [11, 7], '8': [7, 2], '9': [7, 10], '10': [7, 19],
    '11': [7, 10], '12': [19, 25], '13': [11, 27], '14': [2, 10], '15': [3, 2], '16': [3, 27], '17': [19, 10], '18': [27, 25], '19': [27, 6], '20': [27, 19],
    '21': [1, 23], '22': [16, 4], '23': [19, 13], '24': [3, 22], '25': [5, 26], '26': [27, 10], '27': [27, 3], '28': [27, 19], '29': [1, 20], '30': [2, 24],
    '31': [5, 18], '32': [9, 13], '33': [27, 15], '34': [23, 21], '35': [5, 1], '36': [9, 2], '37': [27, 9], '38': [1, 5], '39': [3, 14], '40': [8, 17],
    '41': [19, 12], '42': [21, 20], '43': [5, 20], '44': [2, 27]
}


def filter_and_save_csv(input_file_path, output_file_path, player_a_id, player_b_id):
    players = {'A': player_a_id, 'B': player_b_id}
    with open(input_file_path, 'r') as input_file, open(output_file_path, 'w', newline='') as output_file:
        csv_reader = csv.reader(input_file)
        csv_writer = csv.writer(output_file)
        index = 0
        for row in csv_reader:
            # Example condition: Keep rows where the first column is 'True'
            if index == 0:
                row.append('opponent')
                csv_writer.writerow(row)
            else:
                row[8] = shot_types[row[8]]
                if len(row[19]) > 0:
                    row[19] = reasons[row[19]]
                if len(row[20]) > 0:
                    row[20] = reasons[row[20]]
                key = row[6]
                row.append(sum(players.values()) - players[key])
                row[6] = players[key]
                csv_writer.writerow(row)
            index+=1

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <input_file_path> <output_file_path> <match_id>")
        sys.exit(1)

    input_file_path = sys.argv[1]
    output_file_path = sys.argv[2]
    match_id = sys.argv[3]
    
    filter_and_save_csv(input_file_path, output_file_path, matches[match_id][0], matches[match_id][1])
