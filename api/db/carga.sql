
CREATE database IF NOT EXISTS estoque;

INSERT INTO public.estoque_item
(uuid, title, price, description, created_on, type_item, estoque_id)
VALUES('56a8266e-b1ee-11ed-afa1-0242ac120002', 'caneta', 0, 'canetas', '', 'Nao Perecivel', NULL);

INSERT INTO public.estoque_item
(uuid, title, price, description, created_on, type_item, estoque_id)
VALUES('99113f80-b1f4-11ed-afa1-0242ac120002', '', 0, '', '', '', 0);

INSERT INTO public.estoque_item
(uuid, title, price, description, created_on, type_item, estoque_id)
VALUES(?, '', 0, '', '', '', 0);

INSERT INTO public.estoque_item
(uuid, title, price, description, created_on, type_item, estoque_id)
VALUES(?, '', 0, '', '', '', 0);

INSERT INTO public.estoque_item
(uuid, title, price, description, created_on, type_item, estoque_id)
VALUES(?, '', 0, '', '', '', 0);

INSERT INTO public.estoque_item
(uuid, title, price, description, created_on, type_item, estoque_id)
VALUES(?, '', 0, '', '', '', 0);

