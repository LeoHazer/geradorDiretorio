import os
import json


def criaDiretorio(caminhoDiretorio):
    arvDiretorio = {
        'nome': os.path.basename(caminhoDiretorio),
        'tipo': 'diretorio',
        'arquivos': []
    }

    for item in os.listdir(caminhoDiretorio):
        item_dir = os.path.join(caminhoDiretorio, item)
        item_info = {
            'nome': item,
            'tipo': '',
            'arquivos': []
        }

        if os.path.isfile(item_dir):
            item_info['tipo'] = geraTipoArq(item_dir)
        else:
            item_info['tipo'] = 'diretorio'
            item_info['arquivos'] = criaDiretorio(item_dir)['arquivos']

        arvDiretorio['arquivos'].append(item_info)

    return arvDiretorio

def geraTipoArq(dirArq):
    extensaoArq = os.path.splitext(dirArq)[1][1:].lower()
    if extensaoArq in ('mp3', 'wav', 'flac'):
        return 'musica'
    elif extensaoArq in ('txt', 'doc', 'pdf', 'xlsx', 'docx'):
        return 'documento'
    elif extensaoArq in ('jpg', 'png', 'gif', 'bmp'):
        return 'imagem'
    else:
        return 'arquivo'

def salvaDiretorio(arvDiretorio, json_arq):
    with open(json_arq, 'w') as f:
        json.dump(arvDiretorio, f, indent=4)
        
        
def main():
    
    os.system("cls")
    
    caminhoDiretorio = input("Entre com o diretório: ")
    saidaJSON = input("Digite o nome do arquivo de saída: ")
    
    # Cria a árvore de diretório
    arvoreDir = criaDiretorio(caminhoDiretorio)
    
    # Save the directory tree to a JSON file
    salvaDiretorio(arvoreDir, saidaJSON)
    
    print("Diretório criado com sucesso!")

if __name__ == "__main__":
    main()

