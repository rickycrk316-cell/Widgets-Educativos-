import * as React from 'react';

export interface TitularProps extends React.HTMLAttributes<HTMLHeadingElement> {
  children?: React.ReactNode;
  /** Escala tipográfica: «portada» 140 px, «feed» 112 px (titular de lámina interior), «seccion» 64 px. */
  nivel?: 'portada' | 'feed' | 'seccion';
  /** Etiqueta HTML. */
  como?: 'h1' | 'h2' | 'h3' | 'p';
}

/** Titular en Fraunces SemiBold; toma el color de acento del fondo de la Lamina (ladrillo sobre hueso, hueso sobre ladrillo y tinta, profundo sobre molde). */
export function Titular({ children, nivel = 'feed', como: Tag = 'h2', className, ...rest }: TitularProps) {
  return (
    <Tag {...rest} className={['atv-titular', `atv-titular-${nivel}`, className].filter(Boolean).join(' ')}>
      {children}
    </Tag>
  );
}
