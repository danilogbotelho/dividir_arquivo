import os
from gooey import Gooey, GooeyParser


def dividir_arquivo(arquivo, max_linhas, destino=None):
    """Divide um arquivo em partes limitadas ao número de linhas especificadas.

    As partes são nomeadas de acordo com o nome do arquivo original com o
    número de ordem do arquivo gerado entre o nome e a extensão, e.g.:

    arquivo.txt com 2000 linhas e max_linhas=1000
    arquivo1.txt e arquivo2.txt terão 1000 linhas cada.

    Se destino não for informado, usa a mesma pasta do arquivo original.

    """

    with open(arquivo, "rt") as f:
        linhas = f.readlines()

    total_linhas = len(linhas)
    gravadas = 0
    numero_arquivo = 0

    caminho_original, nome_original = os.path.split(arquivo)
    nome_base, ext_base = os.path.splitext(nome_original)

    if destino is None:
        destino = caminho_original

    while gravadas < total_linhas:
        numero_arquivo += 1
        nome_arquivo_dest = os.path.join(
            destino, f"{nome_base}{numero_arquivo}{ext_base}"
        )
        with open(nome_arquivo_dest, "wt") as f:
            f.writelines(linhas[gravadas : gravadas + max_linhas])
        gravadas += max_linhas


@Gooey(language="portuguese")
def main():
    parser = GooeyParser(
        description="Divide um arquivo em outros com no máximo um número estipulado de linhas.",
    )
    parser.add_argument(
        "arquivo", help="o caminho para o arquivo a ser dividido", widget="FileChooser"
    )
    parser.add_argument(
        "-l",
        "--linhas",
        default=1000,
        type=int,
        help="o número máximo de linhas por arquivo",
    )
    parser.add_argument(
        "-d",
        "--destino",
        help="especifica uma pasta de destino para os arquivos. Se não especificada, usa a pasta do arquivo original.",
        widget="DirChooser",
    )

    args = parser.parse_args()

    dividir_arquivo(args.arquivo, max_linhas=args.linhas, destino=args.destino)


if __name__ == "__main__":
    main()
