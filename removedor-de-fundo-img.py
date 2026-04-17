import os
from rembg import remove # Importa a função de remoção de fundo
from PIL import Image    # Biblioteca padrão para manipulação de imagens
import io

# --- CONFIGURAÇÃO DE DIRETÓRIOS ---
# r"" antes da string trata o caminho como 'raw', evitando erros com as barras \ do Windows
PASTA_ORIGEM = r"E:\Trabalho\MiauMiauMiau\icon" 
PASTA_DESTINO = r"E:\Trabalho\MiauMiauMiau\icon_limpos"

def limpar_assets_miau():
    # Verifica se a pasta de destino existe, se não, cria.
    if not os.path.exists(PASTA_DESTINO):
        os.makedirs(PASTA_DESTINO)
        print(f"🐾 Pasta criada: {PASTA_DESTINO}")

    print("🚀 Iniciando processamento dos gatinhos...")

    # Loop para percorrer todos os arquivos da pasta de origem
    for nome_arquivo in os.listdir(PASTA_ORIGEM):
        # Filtra apenas arquivos de imagem
        if nome_arquivo.lower().endswith(('.png', '.jpg', '.jpeg')):
            
            caminho_input = os.path.join(PASTA_ORIGEM, nome_arquivo)
            caminho_output = os.path.join(PASTA_DESTINO, nome_arquivo)
            
            print(f"🧼 Removendo fundo de: {nome_arquivo}")

            try:
                # 1. Abre o arquivo em modo de leitura binária ('rb')
                with open(caminho_input, 'rb') as i:
                    input_data = i.read()
                    
                    # 2. A biblioteca rembg analisa os pixels e remove o fundo
                    # Ela identifica o contraste do objeto principal (o gatinho)
                    output_data = remove(input_data)
                    
                # 3. Salva o resultado (agora com canal Alfa/Transparência) na pasta de destino
                with open(caminho_output, 'wb') as o:
                    o.write(output_data)
                    
            except Exception as e:
                print(f"❌ Erro ao processar {nome_arquivo}: {e}")

    print(f"\n✅ Sucesso! Os ícones estão prontos para o App em: {PASTA_DESTINO}")

if __name__ == "__main__":
    limpar_assets_miau()
