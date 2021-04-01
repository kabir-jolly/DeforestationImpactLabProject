def get_ordered_cols(election_type):
    if election_type == "local":
        local_ordered_columns = ['NOME_MUNICIPIO', 'ANO_ELEICAO', 'NUM_TURNO', 'DESCRICAO_ELEICAO', 'SIGLA_UF', 'SIGLA_UE',
       'CODIGO_MUNICIPIO', 'CODIGO_CARGO',
       'NUMERO_CAND', 'SQ_CANDIDATO', 'NOME_CANDIDATO', 'NOME_URNA_CANDIDATO',
       'DESCRICAO_CARGO', 'COD_SIT_CAND_SUPERIOR', 'DESC_SIT_CAND_SUPERIOR',
       'CODIGO_SIT_CANDIDATO', 'DESC_SIT_CANDIDATO', 'CODIGO_SIT_CAND_TOT',
       'DESC_SIT_CAND_TOT', 'NUMERO_PARTIDO', 'SIGLA_PARTIDO', 'NOME_PARTIDO',
       'SEQUENCIAL_LEGENDA', 'NOME_COLIGACAO', 'COMPOSICAO_LEGENDA',
       'TOTAL_VOTOS']
        return local_ordered_columns
    
    elif election_type == "federal":
        federal_ordered_columns = []
        return federal_ordered_columns
    
    else:
        raise ValueError("Argument input was invalid, accepted param values are 'local' and 'federal'")
        
def get_positions(election_type):
    if election_type == "local":
        local_positions = ["VEREADOR", "PREFEITO"]
        return local_positions
    
    elif election_type == "federal":
        federal_positions = []
        return federal_positions
    
    else:
        raise ValueError("Argument input was invalid, accepted param values are 'local' and 'federal'")