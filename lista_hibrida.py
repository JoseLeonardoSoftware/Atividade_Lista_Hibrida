"""Implementação da lista híbrida: região ordenada + cauda não ordenada.

A estrutura mantém as chaves únicas. A região principal permanece ordenada;
as novas chaves são acumuladas no fim da cauda até atingir dez elementos.
"""

import random
from dataclasses import dataclass
from typing import Optional


@dataclass
class ResultadoBusca:
    """Guarda o resultado da busca e as comparações realizadas."""

    encontrada: bool
    chave: int
    local: str
    iteracoes_binaria: int
    iteracoes_sequencial: int

    @property
    def total_iteracoes(self) -> int:
        return self.iteracoes_binaria + self.iteracoes_sequencial


class ListaHibrida:
    """Lista híbrida com região ordenada e cauda de até dez chaves."""

    TAMANHO_INICIAL = 1024
    CAPACIDADE_CAUDA = 10

    def __init__(self, semente: int = 42):
        self.semente = semente
        self.regiao_ordenada = self._gerar_regiao_inicial(semente)
        self.cauda = []
        self.total_reorganizacoes = 0

    @staticmethod
    def _gerar_regiao_inicial(semente: int) -> list[int]:
        """Gera 1.024 inteiros distintos de forma reproduzível."""
        gerador = random.Random(semente)
        numeros = gerador.sample(range(1, 1_000_001), 1024)
        return sorted(numeros)

    def inserir(self, chave: int) -> tuple[bool, str]:
        """Insere no fim da cauda; rejeita repetidas em qualquer região."""
        if not isinstance(chave, int) or isinstance(chave, bool):
            return False, "A chave precisa ser um número inteiro."

        if chave in self.regiao_ordenada or chave in self.cauda:
            return False, f"A chave {chave} já existe na lista."

        if len(self.cauda) >= self.CAPACIDADE_CAUDA:
            # Proteção adicional: em condições normais, a décima chave
            # já dispara a reorganização automaticamente.
            self.reorganizar()

        self.cauda.append(chave)

        if len(self.cauda) == self.CAPACIDADE_CAUDA:
            self.reorganizar()
            return True, (
                f"Chave {chave} inserida. A cauda chegou a dez elementos "
                "e foi reorganizada automaticamente."
            )

        return True, f"Chave {chave} inserida no final da cauda."

    def buscar(self, chave: int) -> ResultadoBusca:
        """Busca primeiro na região ordenada e depois na cauda."""
        inicio, fim = 0, len(self.regiao_ordenada) - 1
        iteracoes_binaria = 0

        while inicio <= fim:
            meio = (inicio + fim) // 2
            iteracoes_binaria += 1
            valor = self.regiao_ordenada[meio]

            if valor == chave:
                return ResultadoBusca(
                    True, chave, "Região ordenada (busca binária)",
                    iteracoes_binaria, 0
                )
            if valor < chave:
                inicio = meio + 1
            else:
                fim = meio - 1

        iteracoes_sequencial = 0
        for valor in self.cauda:
            iteracoes_sequencial += 1
            if valor == chave:
                return ResultadoBusca(
                    True, chave, "Cauda não ordenada (busca sequencial)",
                    iteracoes_binaria, iteracoes_sequencial
                )

        return ResultadoBusca(
            False, chave, "Não encontrada",
            iteracoes_binaria, iteracoes_sequencial
        )

    def reorganizar(self) -> None:
        """Ordena a cauda e intercala seus valores na região principal."""
        if not self.cauda:
            return

        cauda_ordenada = sorted(self.cauda)
        principal = self.regiao_ordenada
        resultado = []
        i = j = 0

        # Intercala as duas sequências já ordenadas sem chamar sort()
        # sobre a lista inteira.
        while i < len(principal) and j < len(cauda_ordenada):
            if principal[i] <= cauda_ordenada[j]:
                resultado.append(principal[i])
                i += 1
            else:
                resultado.append(cauda_ordenada[j])
                j += 1

        resultado.extend(principal[i:])
        resultado.extend(cauda_ordenada[j:])

        self.regiao_ordenada = resultado
        self.cauda.clear()
        self.total_reorganizacoes += 1

    def contem(self, chave: int) -> bool:
        """Informa se a chave está em qualquer uma das regiões."""
        return chave in self.regiao_ordenada or chave in self.cauda

    @property
    def quantidade_total(self) -> int:
        return len(self.regiao_ordenada) + len(self.cauda)

    def validar_invariantes(self) -> bool:
        """Confere ordenação, unicidade e limite da cauda."""
        principal_ordenada = all(
            self.regiao_ordenada[i] <= self.regiao_ordenada[i + 1]
            for i in range(len(self.regiao_ordenada) - 1)
        )
        todas = self.regiao_ordenada + self.cauda
        sem_repeticoes = len(todas) == len(set(todas))
        cauda_no_limite = len(self.cauda) <= self.CAPACIDADE_CAUDA
        return principal_ordenada and sem_repeticoes and cauda_no_limite
