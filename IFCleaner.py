import ifcopenshell
import ifcopenshell.util.element

def clean_ifc(input_path, output_path):
    # Carregar arquivo IFC
    model = ifcopenshell.open(input_path)
    
    elements_to_remove = []

    # 1. Remover geometria desnecessária
    for element in model.by_type("IfcProduct"):
        if not element.Representation:  # Sem representação geométrica
            elements_to_remove.append(element)

    # 2. Remover propriedades redundantes
    for prop_set in model.by_type("IfcPropertySet"):
        if not ifcopenshell.util.element.get_referenced_elements(prop_set):
            elements_to_remove.append(prop_set)

    # 3. Remover relacionamentos não usados
    for rel in model.by_type("IfcRelAssociates"):
        if not rel.RelatedObjects:
            elements_to_remove.append(rel)

    # 4. Remover estilos visuais
    for style in model.by_type("IfcStyledItem"):
        elements_to_remove.append(style)

    # 5. Reduzir precisão numérica
    for point in model.by_type("IfcCartesianPoint"):
        point.Coordinates = [round(coord, 6) for coord in point.Coordinates]

    # 6. Filtrar elementos distantes
    central_point = [0, 0, 0]  # Defina o ponto central
    max_distance = 100  # Distância máxima permitida
    for product in model.by_type("IfcProduct"):
        if product.ObjectPlacement:
            placement = product.ObjectPlacement.RelativePlacement.Location
            distance = sum((coord - central_coord) ** 2 for coord, central_coord in zip(placement.Coordinates, central_point)) ** 0.5
            if distance > max_distance:
                elements_to_remove.append(product)

    # Eliminar elementos identificados
    for element in set(elements_to_remove):  # Usar set para evitar duplicatas
        model.remove(element)
    
    # Salvar arquivo limpo
    model.write(output_path)
    print(f"Arquivo salvo como '{output_path}'. {len(elements_to_remove)} elementos removidos.")

# Uso
clean_ifc("SEU IFC AQUI.ifc", "IFC_LIMPO.ifc")
