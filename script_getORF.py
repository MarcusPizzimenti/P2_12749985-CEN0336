#!/usr/binenv python3

import sys
import re
from Bio import SeqIO

# Função para encontrar os ORFs
def find_orfs(sequence):
    try:
        # Definindo os códons de início e terminação
        start_codons = ["ATG"]
        stop_codons = ["TAA", "TAG", "TGA"]
        
        orfs = []
        
        # Para cada uma das 6 fases de leitura possíveis
        for frame in range(6):
            orf = ""
            for i in range(frame, len(sequence), 3):
                codon = sequence[i:i+3]
                if codon in start_codons:
                    # Encontrou um códon de início, iniciar um ORF
                    orf_start = i
                if codon in stop_codons and len(orf) > 0:
                    # Encontrou um códon de parada, terminar o ORF
                    orf_end = i + 3
                    orfs.append((orf_start, orf_end, sequence[orf_start:orf_end]))
                    orf = ""
        
        # Caso não tenha encontrado nenhum ORF válido
        if not orfs:
            raise ValueError("Nenhum ORF válido encontrado na sequência.")
        
        return orfs
    except Exception as e:
        print(f"Erro ao procurar ORFs: {e}")
        sys.exit(1)

def main():
    try:
        # Lê o arquivo multifasta da linha de comando
        if len(sys.argv) != 2:
            raise ValueError("Por favor, forneça o caminho para o arquivo multifasta.")
        
        input_file = sys.argv[1]
        
        # Verificando se o arquivo existe
        try:
            records = SeqIO.parse(input_file, "fasta")
        except FileNotFoundError:
            raise FileNotFoundError(f"Arquivo {input_file} não encontrado.")
        except Exception as e:
            raise Exception(f"Erro ao ler o arquivo {input_file}: {e}")
        
        # Processa cada sequência no arquivo
        for record in records:
            seq = str(record.seq)
            try:
                # Chama a função find_orfs para encontrar os ORFs
                orfs = find_orfs(seq)
                
                # Seleciona o ORF mais longo
                longest_orf = max(orfs, key=lambda x: len(x[2]))
                
                # Extrai informações sobre o ORF mais longo
                start, end, sequence = longest_orf
                
                # Escreve os arquivos ORF.fna e ORF.faa
                with open("ORF.fna", "a") as fna_file:
                    fna_file.write(f">{record.id}_frame{start}_{end}\n{sequence}\n")
                
                # Converte o ORF em peptídeo
                peptide = sequence.translate()  # Traduz a sequência para o peptídeo

                with open("ORF.faa", "a") as faa_file:
                    faa_file.write(f">{record.id}_frame{start}_{end}\n{peptide}\n")
            
            except Exception as e:
                print(f"Erro ao processar a sequência {record.id}: {e}")
                continue  # Continua com a próxima sequência

    except Exception as e:
        print(f"Erro geral: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()

