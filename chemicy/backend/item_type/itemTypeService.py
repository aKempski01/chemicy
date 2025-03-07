from typing import Tuple, List, Dict, Optional

import reflex as rx

def validate_cas(cas_number: str) -> bool:
    if cas_number == "11-120" or cas_number == "11-130":
        return True
    return False

def get_p_h_codes_for_cas(cas_number: str) -> Dict[str, List[str]]:
    if cas_number == "11-120":
        return {"h_codes": ['H302', 'H314', 'H317'], "p_codes":['P261', 'P272', 'P280', 'P301 + P312, P303 + P361 + P353', 'P305 + P351 + P338']}
    elif cas_number == "11-130":
        return {"h_codes": ['H352', 'H3112', 'H398'],
                "p_codes": ['P223', 'P272', 'P289', 'P301 + P303 + P361 + P353', 'P305 + P351 + P338']}
    else:
        return {"h_codes":[],
                "p_codes": []}
