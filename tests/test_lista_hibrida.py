import unittest
import sys
from pathlib import Path

# Permite executar os testes tanto pela raiz do projeto quanto pela pasta tests.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from lista_hibrida import ListaHibrida


class TestListaHibrida(unittest.TestCase):

    def test_gera_1024_numeros_distintos_e_ordenados(self):
        lista = ListaHibrida(semente=123)
        self.assertEqual(len(lista.regiao_ordenada), 1024)
        self.assertEqual(len(set(lista.regiao_ordenada)), 1024)
        self.assertEqual(lista.regiao_ordenada, sorted(lista.regiao_ordenada))

    def test_semente_garante_reprodutibilidade(self):
        primeira = ListaHibrida(semente=77)
        segunda = ListaHibrida(semente=77)
        self.assertEqual(primeira.regiao_ordenada, segunda.regiao_ordenada)

    def test_sementes_diferentes_geram_listas_diferentes(self):
        primeira = ListaHibrida(semente=77)
        segunda = ListaHibrida(semente=78)
        self.assertNotEqual(primeira.regiao_ordenada, segunda.regiao_ordenada)

    def test_insere_no_final_da_cauda_sem_ordenar(self):
        lista = ListaHibrida()
        lista.inserir(2_000_001)
        lista.inserir(-10)
        self.assertEqual(lista.cauda, [2_000_001, -10])

    def test_rejeita_chave_repetida_na_regiao_principal(self):
        lista = ListaHibrida()
        chave = lista.regiao_ordenada[0]
        sucesso, _ = lista.inserir(chave)
        self.assertFalse(sucesso)
        self.assertEqual(lista.cauda, [])

    def test_rejeita_chave_repetida_na_cauda(self):
        lista = ListaHibrida()
        lista.inserir(2_000_001)
        sucesso, _ = lista.inserir(2_000_001)
        self.assertFalse(sucesso)
        self.assertEqual(lista.cauda, [2_000_001])

    def test_busca_binaria_encontra_na_regiao(self):
        lista = ListaHibrida()
        chave = lista.regiao_ordenada[500]
        resultado = lista.buscar(chave)
        self.assertTrue(resultado.encontrada)
        self.assertIn("binária", resultado.local)
        self.assertGreater(resultado.iteracoes_binaria, 0)
        self.assertEqual(resultado.iteracoes_sequencial, 0)

    def test_busca_sequencial_encontra_na_cauda(self):
        lista = ListaHibrida()
        lista.inserir(2_000_001)
        resultado = lista.buscar(2_000_001)
        self.assertTrue(resultado.encontrada)
        self.assertIn("Cauda", resultado.local)
        self.assertGreater(resultado.iteracoes_binaria, 0)
        self.assertEqual(resultado.iteracoes_sequencial, 1)

    def test_busca_informa_nao_encontrada_e_total(self):
        lista = ListaHibrida()
        resultado = lista.buscar(-99)
        self.assertFalse(resultado.encontrada)
        self.assertEqual(
            resultado.total_iteracoes,
            resultado.iteracoes_binaria + resultado.iteracoes_sequencial
        )

    def test_decima_insercao_reorganiza_e_esvazia_cauda(self):
        lista = ListaHibrida()
        for numero in range(2_000_001, 2_000_011):
            sucesso, _ = lista.inserir(numero)
            self.assertTrue(sucesso)
        self.assertEqual(lista.cauda, [])
        self.assertEqual(len(lista.regiao_ordenada), 1034)
        self.assertEqual(lista.total_reorganizacoes, 1)
        self.assertEqual(lista.regiao_ordenada, sorted(lista.regiao_ordenada))

    def test_novas_insercoes_sao_permitidas_apos_reorganizacao(self):
        lista = ListaHibrida()
        for numero in range(2_000_001, 2_000_011):
            lista.inserir(numero)
        sucesso, _ = lista.inserir(3_000_001)
        self.assertTrue(sucesso)
        self.assertEqual(lista.cauda, [3_000_001])

    def test_reorganizacao_preserva_todas_as_chaves(self):
        lista = ListaHibrida()
        originais = set(lista.regiao_ordenada)
        novas = set(range(2_000_001, 2_000_011))
        for numero in novas:
            lista.inserir(numero)
        self.assertEqual(set(lista.regiao_ordenada), originais | novas)

    def test_invariantes_permanecem_validas(self):
        lista = ListaHibrida()
        for numero in range(2_000_001, 2_000_006):
            lista.inserir(numero)
        self.assertTrue(lista.validar_invariantes())


if __name__ == "__main__":
    unittest.main()
