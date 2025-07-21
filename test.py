def dict_check(word):
    try:
        # Use subprocess for cleaner grep processing
        import subprocess
        
        # First, find lexical senses for this word
        result = subprocess.run(['grep', '-B', '1', '-A', '1', f'lemma/{word}#', 'english-wordnet-2024.ttl'], 
                              capture_output=True, text=True)
        
        if result.returncode != 0:
            return False
        
        # Parse the grep output to find synset IDs
        synset_ids = []
        lines = result.stdout.split('\n')
        
        for line in lines:
            line = line.strip()
            if 'ontolex:isLexicalizedSenseOf' in line and 'wnid:' in line:
                start = line.find('wnid:') + 5
                end = line.find(' ', start)
                if end == -1:
                    end = line.find('.', start)
                if end == -1:
                    end = len(line)
                synset_id = line[start:end].strip(' .')
                if synset_id not in synset_ids:
                    synset_ids.append(synset_id)
        
        if not synset_ids:
            return False
        
        # Now find definitions for the first synset
        for synset_id in synset_ids:
            # Use grep to find the synset definition
            def_result = subprocess.run(['grep', '-A', '10', f'wnid:{synset_id}', 'english-wordnet-2024.ttl'], 
                                      capture_output=True, text=True)
            
            if def_result.returncode == 0:
                def_lines = def_result.stdout.split('\n')
                for line in def_lines:
                    if 'rdf:value' in line and '"' in line:
                        value_start = line.find('rdf:value "')
                        if value_start != -1:
                            start = value_start + 11
                            end = line.find('"@en', start)
                            if end == -1:
                                end = line.find('"', start)
                            if end != -1:
                                return line[start:end]
        
        return f"Word '{word}' found but no definition available"
    
    except Exception as e:
        print(f"Error: {e}")
        return False


print(dict_check('grave'))